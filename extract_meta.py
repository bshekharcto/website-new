import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
pages = [
    "index.html",
    "pages/solutions/highway.html",
    "pages/solutions/mining.html",
    "pages/solutions/water.html",
    "pages/solutions/ehs.html",
    "pages/platform/boson.html",
    "pages/platform/photon.html",
    "pages/platform/cortex.html"
]

print("CURRENT META DESCRIPTIONS:")
for p in pages:
    filepath = os.path.join(BASE_DIR, p)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content=["\']([^"\']*)["\']\s+name=["\']description["\']', html, re.IGNORECASE)
        
    if desc_match:
        desc = desc_match.group(1)
        print(f"{p}: ({len(desc)} chars)\n{desc}\n")
    else:
        print(f"{p}: MISSING\n")
