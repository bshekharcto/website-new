import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"

for root, dirs, files in os.walk(BASE_DIR):
    if 'raw_html' in root:
        continue
        
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Replace Mega Menu 'Blog & Insights' Title
            content = content.replace('<div class="mega-aud-title">Blog &amp; Insights</div>', '<div class="mega-aud-title">News &amp; Insights</div>')
            
            # Since relative paths differ, let's just do a regex replace for the href
            # Find the section:
            # <!-- Blog & Insights -->
            # <a href="some/path/index.html" class="mega-aud-card">
            
            def replace_href(match):
                href = match.group(1)
                # If it already has #news, ignore
                if '#news' not in href:
                    return f'<!-- Blog & Insights -->\n                  <a href="{href}#news" class="mega-aud-card">'
                return match.group(0)
                
            content = re.sub(r'<!-- Blog & Insights -->\s*<a href="([^"]+)" class="mega-aud-card">', replace_href, content)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Updated Mega Menu links globally.")
