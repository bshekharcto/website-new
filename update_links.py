import os
import re

for root, _, files in os.walk('.'):
    if 'raw_html' in root: continue
    for f in files:
        if not f.endswith('.html'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Determine relative path
        rel = '../../' if any(x in root.replace('\\', '/') for x in ['pages/platform', 'pages/solutions', 'pages/customers', 'pages/resources']) else ''
        res_link = rel + 'pages/resources/index.html'
        
        # Replace "Browse all" link under resources
        content = re.sub(
            r'<a href="[^"]*" style="font-family:var\(--display\);font-size:12px;font-weight:700;color:var\(--blue\);">Browse all',
            f'<a href="{res_link}" style="font-family:var(--display);font-size:12px;font-weight:700;color:var(--blue);">Browse all',
            content
        )
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
