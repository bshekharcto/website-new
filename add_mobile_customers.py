import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'mobile-menu-title">Customers<' in content:
            continue
            
        # Find prefix
        # It's either pages/customers/index.html or ../customers/index.html etc
        # Usually inside the Resources section we have: <a href="PREFIXcustomers/index.html">Customer Stories</a>
        m = re.search(r'href="([^"]*?)customers/index\.html"', content)
        prefix = m.group(1) if m else 'pages/'
        
        # Build the customers block
        customers_block = f"""      <div class="mobile-menu-section">
        <div class="mobile-menu-title">Customers</div>
        <div class="mobile-menu-links">
          <a href="{prefix}customers/index.html">All Customers</a>
          <a href="{prefix}customers/uprrda-case-study.html">UPRRDA</a>
          <a href="{prefix}customers/canyon.html">Crayon Resources</a>
          <a href="{prefix}customers/watco.html">Odisha Water Authority</a>
          <a href="{prefix}customers/hindalco.html">Hindalco</a>
          <a href="{prefix}customers/nrida.html">NRIDA</a>
        </div>
      </div>
"""
        
        # Insert before Resources section
        # Look for <div class="mobile-menu-section">\s*<div class="mobile-menu-title">Resources</div>
        target_regex = r'(<div class="mobile-menu-section">\s*<div class="mobile-menu-title">Resources</div>)'
        
        if re.search(target_regex, content):
            new_content = re.sub(target_regex, customers_block + r'\1', content, count=1)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Skipped {filepath} (Resources section not found)")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
