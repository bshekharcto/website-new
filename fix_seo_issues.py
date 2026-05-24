import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
html_files = []
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".html") and "raw_html" not in root:
            html_files.append(os.path.join(root, file))

robots_meta = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'

def add_lazy_loading(match):
    img_tag = match.group(0)
    # Skip if already has loading=
    if 'loading=' in img_tag:
        return img_tag
    # Skip logos or header images that shouldn't be lazy loaded
    if 'logo' in img_tag.lower():
        return img_tag
        
    # Insert loading="lazy" before the closing bracket
    if img_tag.endswith('/>'):
        return img_tag[:-2] + ' loading="lazy"/>'
    else:
        return img_tag[:-1] + ' loading="lazy">'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    
    # 1. Add robots meta if missing
    if '<meta name="robots"' not in html and '</head>' in html:
        html = html.replace('</head>', f'    {robots_meta}\n</head>')
        modified = True
        
    # 2. Add loading="lazy" to images
    new_html = re.sub(r'<img\s+[^>]+>', add_lazy_loading, html, flags=re.IGNORECASE)
    if new_html != html:
        html = new_html
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated: {os.path.relpath(filepath, BASE_DIR)}")
