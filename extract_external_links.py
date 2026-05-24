import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"

def find_external_links():
    links = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # We will INCLUDE raw_html this time
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, BASE_DIR)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find all <a> tags
                a_tags = re.findall(r'<a[^>]+href=["\'](http[s]?://[^"\']+)["\'][^>]*>(.*?)</a>', content, re.IGNORECASE | re.DOTALL)
                
                for href, text in a_tags:
                    # Ignore internal links and common schema/fonts
                    if any(domain in href for domain in ['cognecto.com', 'localhost', 'schema.org', 'fonts.googleapis', 'fonts.gstatic', 'w3.org']):
                        continue
                        
                    # Clean up text
                    text_clean = re.sub(r'<[^>]+>', '', text).strip()
                    text_clean = re.sub(r'\s+', ' ', text_clean)
                    
                    if not text_clean:
                        # try to get alt text if image
                        img_match = re.search(r'<img[^>]+alt=["\']([^"\']*)["\']', text, re.IGNORECASE)
                        if img_match:
                            text_clean = "[Image] " + img_match.group(1)
                        else:
                            text_clean = "[No Text/Image]"
                            
                    links.append({
                        'file': rel_path,
                        'url': href,
                        'text': text_clean
                    })
                    
    return links

external_links = find_external_links()

unique_links = {}
for link in external_links:
    if link['url'] not in unique_links:
        unique_links[link['url']] = {
            'text': link['text'],
            'files': set()
        }
    unique_links[link['url']]['files'].add(link['file'])
    
md = "# External Articles & References\n\nFound these external links across the codebase (including old `raw_html` files). Please review these to decide which ones should become 'News' articles.\n\n"

for url, data in unique_links.items():
    text_display = data['text']
    files_list = ", ".join(data['files'])
    md += f"### {text_display}\n"
    md += f"- **URL:** {url}\n"
    md += f"- **Found in:** {files_list}\n\n"

output_path = r"C:\Users\bhanu\.gemini\antigravity-ide\brain\da3adee4-6cb0-4a66-a00a-19d04af0e6e0\external_articles.md"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Extracted {len(unique_links)} external links to {output_path}")
