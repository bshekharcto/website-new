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
                
            # Replace Mega Menu 'Customer Stories' Title and Desc
            content = content.replace('<div class="mega-aud-title">Customer Stories</div>', '<div class="mega-aud-title">About Us</div>')
            content = content.replace('<div class="mega-aud-desc">Real deployments and measured outcomes from UPRRDA to \nAustralia</div>', '<div class="mega-aud-desc">The AI Operating System for Physical Infrastructure</div>')
            content = content.replace('<div class="mega-aud-desc">Real deployments and measured outcomes from UPRRDA to Australia</div>', '<div class="mega-aud-desc">The AI Operating System for Physical Infrastructure</div>')
            
            # Replace href for Mega Menu "Customer Stories" -> "About Us"
            def replace_href(match):
                prefix = match.group(1)
                return f'<!-- About Us -->\n                    <a href="{prefix}resources/about-us.html" class="mega-aud-card">'
                
            content = re.sub(r'<!-- Customer Stories -->\s*<a href="([^"]*)customers/index.html" class="mega-aud-card">', replace_href, content)
            
            # Replace Mobile menu link under Resources
            def replace_mobile_href(match):
                prefix = match.group(1)
                return f'<a href="{prefix}resources/about-us.html">About Us</a>'
                
            # The mobile menu link is usually preceded by <div class="mobile-menu-title">Resources</div> and then <div class="mobile-menu-links">
            # A simple regex for just that link:
            # We want to replace <a href=".../customers/index.html">Customer Stories</a>
            # But only the one that is "Customer Stories", since there might be a main menu link for "Customer Stories" as a section itself.
            content = re.sub(r'<a href="([^"]*)customers/index.html">\s*Customer Stories\s*</a>', replace_mobile_href, content)
            
            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Replaced Customer Stories with About Us in the Resources drop-down globally.")
