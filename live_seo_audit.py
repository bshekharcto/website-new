import urllib.request
import re
from urllib.error import URLError, HTTPError
from urllib.parse import urljoin

BASE_URL = "https://www.cognecto.com"

pages_to_audit = [
    "/",
    "/pages/solutions/mining.html",
    "/pages/platform/boson.html",
    "/about-us",  # Check redirect
]

def analyze_html(html, url):
    issues = []
    
    # Title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else None
    if not title:
        issues.append("Missing <title> tag")
    elif len(title) > 60:
        issues.append(f"Title too long ({len(title)} chars) - keep under 60")
        
    # Meta Description
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
    
    desc = desc_match.group(1).strip() if desc_match else None
    if not desc:
        issues.append("Missing meta description")
    elif len(desc) < 120 or len(desc) > 160:
        issues.append(f"Meta description length ({len(desc)} chars) is not optimal (aim for 120-160)")
        
    # H1
    h1_count = len(re.findall(r'<h1[^>]*>', html, re.IGNORECASE))
    if h1_count == 0:
        issues.append("Missing <h1> tag")
    elif h1_count > 1:
        issues.append(f"Multiple <h1> tags found ({h1_count}) - should only have 1")
        
    # Canonical
    if '<link rel="canonical"' not in html.lower():
        issues.append("Missing canonical tag")
        
    # JSON-LD Schema
    schema_count = len(re.findall(r'<script type=["\']application/ld\+json["\']', html, re.IGNORECASE))
    if schema_count == 0:
        issues.append("Missing JSON-LD structured data")
        
    # Image Alt Text
    img_tags = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
    missing_alt = 0
    for img in img_tags:
        if 'alt=' not in img.lower():
            missing_alt += 1
    if missing_alt > 0:
        issues.append(f"{missing_alt} images missing alt text")
        
    # Open Graph Tags
    if '<meta property="og:title"' not in html.lower():
        issues.append("Missing Open Graph (og:title) tags")
        
    return {
        "url": url,
        "title": title,
        "issues": issues,
        "schema_count": schema_count,
        "img_count": len(img_tags)
    }

print("Starting Live SEO Audit of " + BASE_URL)
print("-" * 50)

# 1. Check robots.txt
try:
    req = urllib.request.Request(BASE_URL + "/robots.txt", headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    robots = response.read().decode('utf-8')
    print("ROBOTS.TXT: Found")
    if "User-agent: GPTBot" in robots or "User-agent: PerplexityBot" in robots:
        print("  ✓ AI bots explicitly allowed")
    else:
        print("  ! AI bots not explicitly mentioned")
except HTTPError as e:
    print(f"ROBOTS.TXT: Error {e.code}")
except Exception as e:
    print(f"ROBOTS.TXT: Error {e}")

print("-" * 50)

# 2. Check sitemap.xml
try:
    req = urllib.request.Request(BASE_URL + "/sitemap.xml", headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    sitemap = response.read().decode('utf-8')
    print("SITEMAP.XML: Found")
    loc_count = len(re.findall(r'<loc>', sitemap))
    print(f"  ✓ Contains {loc_count} URLs")
except HTTPError as e:
    print(f"SITEMAP.XML: Error {e.code}")
except Exception as e:
    print(f"SITEMAP.XML: Error {e}")

print("-" * 50)

# 3. Analyze specific pages
for path in pages_to_audit:
    url = urljoin(BASE_URL, path)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        # Check if redirected
        final_url = response.geturl()
        html = response.read().decode('utf-8', errors='ignore')
        
        status = response.getcode()
        
        print(f"URL: {url}")
        if final_url != url:
            print(f"  -> Redirected to: {final_url}")
            
        print(f"  Status: {status}")
        
        if status == 200:
            analysis = analyze_html(html, final_url)
            print(f"  Title: {analysis['title']}")
            print(f"  JSON-LD Schemas: {analysis['schema_count']}")
            print(f"  Images found: {analysis['img_count']}")
            if not analysis['issues']:
                print("  ✓ No critical on-page SEO issues found")
            else:
                for issue in analysis['issues']:
                    print(f"  ! {issue}")
    except HTTPError as e:
        print(f"URL: {url} - Error {e.code}")
    except Exception as e:
        print(f"URL: {url} - Error {e}")
    print("-" * 50)
