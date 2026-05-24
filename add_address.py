import os
import glob

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
html_files = glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True)

address_html = """
    <div style="width:100%; margin-bottom:1.5rem; padding-bottom:1.5rem; border-bottom:1px solid rgba(255,255,255,0.08);">
      <div style="font-family:var(--display);font-size:12px;color:rgba(255,255,255,0.4);line-height:1.6;max-width:800px;">
        Address: First Floor, Lobby A, East Wing, Neil Rao Towers, 117 & 118, Rd Number 3, Vijayanagar, EPIP Zone, Whitefield, Bengaluru, Karnataka 560066, India
      </div>
    </div>
    """

count = 0
for filepath in html_files:
    if filepath.endswith('index.html') and os.path.dirname(filepath) == BASE_DIR:
        # Skip the main index.html as it already has the large footer with address
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Check if address is already there
    if 'Neil Rao Towers' in html:
        continue
        
    # Find the footer wrap content
    footer_wrap = html.find('<div class="wrap" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;">')
    
    if footer_wrap != -1:
        # Insert the address html right after the wrap div opens
        insert_pos = footer_wrap + len('<div class="wrap" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem;">')
        new_html = html[:insert_pos] + address_html + html[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated footer in {filepath}")
        count += 1
    else:
        # Some pages might have a different footer format, we check for `<footer`
        footer_idx = html.rfind('<footer')
        if footer_idx != -1:
            wrap_idx = html.find('<div class="wrap"', footer_idx)
            if wrap_idx != -1:
                wrap_end = html.find('>', wrap_idx) + 1
                new_html = html[:wrap_end] + address_html + html[wrap_end:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                print(f"Updated custom footer in {filepath}")
                count += 1

print(f"Added address to {count} pages.")
