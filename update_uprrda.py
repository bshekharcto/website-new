import os
import re

for root, _, files in os.walk('.'):
    if 'raw_html' in root: continue
    for f in files:
        if not f.endswith('.html'): continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace uprrda.html with uprrda-case-study.html
        content = content.replace('uprrda.html', 'uprrda-case-study.html')
        
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
