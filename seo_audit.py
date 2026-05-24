import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
html_files = []
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".html") and "raw_html" not in root:
            html_files.append(os.path.join(root, file))

issues = {
    "missing_h1": [],
    "multiple_h1": [],
    "missing_canonical": [],
    "missing_lang": [],
    "missing_meta_desc": [],
    "images_without_lazy": [],
    "missing_robots_meta": []
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    rel_path = os.path.relpath(filepath, BASE_DIR)
    
    # Check H1
    h1_count = len(re.findall(r'<h1[^>]*>', html, re.IGNORECASE))
    if h1_count == 0:
        issues["missing_h1"].append(rel_path)
    elif h1_count > 1:
        issues["multiple_h1"].append(rel_path)
        
    # Check Canonical
    if '<link rel="canonical"' not in html:
        issues["missing_canonical"].append(rel_path)
        
    # Check Lang
    if '<html lang="en"' not in html:
        issues["missing_lang"].append(rel_path)
        
    # Check Meta Description
    if '<meta name="description"' not in html:
        issues["missing_meta_desc"].append(rel_path)
        
    # Check Images without lazy loading
    imgs = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
    lazy_missing = 0
    for img in imgs:
        if 'loading="lazy"' not in img and 'class="logo"' not in img and 'id="cognecto-nav-logo"' not in img:
            lazy_missing += 1
    if lazy_missing > 5:  # Allow a few hero images to be eager
        issues["images_without_lazy"].append(rel_path)
        
    # Check Robots Meta
    if '<meta name="robots"' not in html:
        issues["missing_robots_meta"].append(rel_path)

print("=== SEO AUDIT RESULTS ===")
for k, v in issues.items():
    print(f"\n{k.upper()}: {len(v)} pages affected")
    for p in v[:5]:
        print(f"  - {p}")
    if len(v) > 5:
        print(f"  - ...and {len(v)-5} more")
