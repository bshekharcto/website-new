import re

def find_mobile_menu():
    with open('index.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = []
    for i, line in enumerate(lines):
        if re.search(r'(mobile|menu|hamburger|nav)', line, re.IGNORECASE):
            out.append(f"{i+1}: {line.strip()[:150]}")
    
    with open('search_results.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

find_mobile_menu()
