import re

html = open('pages/solutions/mining.html', 'r', encoding='utf-8').read()

# Find the body content structure
body_start = html.find('</style>')
body_end = html.find('<script>')

# Get first 3000 chars of body content
body_snippet = html[body_start:body_start+3000]

# Find all opening tags with classes
tags = re.findall(r'<(header|footer|main|nav|article|aside|section|div)\b[^>]*(?:class="([^"]*)")?[^>]*>', body_snippet)
for i, (tag, cls) in enumerate(tags):
    print(f"{i:3d}  <{tag:10s}  class=\"{cls}\"")

print("\n\n--- Looking for img tags ---")
imgs = re.findall(r'<img[^>]*(?:alt="([^"]*)")?[^>]*src="([^"]*)"[^>]*/?\s*>', html[:10000])
for alt, src in imgs[:20]:
    print(f"  alt=\"{alt}\"  src=\"{src}\"")
    
# Also check reverse order
imgs2 = re.findall(r'<img[^>]*src="([^"]*)"[^>]*(?:alt="([^"]*)")?[^>]*/?\s*>', html[:10000])
for src, alt in imgs2[:20]:
    print(f"  src=\"{src}\"  alt=\"{alt}\"")

print("\n\n--- Looking for footer ---")
footer_pos = html.find('<footer')
if footer_pos > 0:
    print(html[footer_pos:footer_pos+500])
else:
    # Find the CTA section or bottom
    print("No <footer> tag found")
    cta_pos = html.rfind('</section>')
    if cta_pos > 0:
        print(html[cta_pos:cta_pos+500])
