import os

directory = r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new'

for root, dirs, files in os.walk(directory):
    if 'raw_html' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.splitlines()
            modified = False
            for i, line in enumerate(lines):
                if '<title>' in line or 'og:title' in line or 'twitter:title' in line:
                    old_line = line
                    line = line.replace(' — ', ' | ')
                    line = line.replace(' – ', ' | ')
                    line = line.replace(' · ', ' | ')
                    line = line.replace(' - ', ' | ')
                    
                    if old_line != line:
                        lines[i] = line
                        modified = True
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines) + '\n')
