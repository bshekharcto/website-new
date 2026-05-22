import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('class="nav-wrap"')
if idx != -1:
    print(content[idx-50:idx+2500])
else:
    print("nav-wrap not found")
