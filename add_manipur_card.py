import base64
import re

html_path = 'pages/customers/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Rename "Border Roads Org." to "BRO"
content = content.replace('<div class="cust-card-name">Border Roads Org.</div>', '<div class="cust-card-name">BRO</div>')

# 2. Add Manipur customer card after BRO
img2_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779430754958.jpg'
try:
    b64_manipur = base64.b64encode(open(img2_path, 'rb').read()).decode('utf-8')
except Exception as e:
    print('Error reading image:', e)
    exit(1)

manipur_card = f"""</a>
        <a href="#" class="cust-card" data-tags="government" data-region="india">
          <div class="cust-card-img" style="background: white; display: flex; align-items: center; justify-content: center; height: 180px;">
            <img src="data:image/jpeg;base64,{b64_manipur}" alt="State of Manipur" style="max-height: 80px; max-width: 80%; object-fit: contain;" loading="lazy"/>
            <div class="cust-card-img-overlay" style="background:linear-gradient(160deg,rgba(14,27,53,0.05) 0%,#2E4DEA33 100%);"></div>
            <div class="cust-card-stat">
              <div class="cust-card-stat-n" style="color:#2E4DEA;">New</div>
              <div class="cust-card-stat-l">Government Partner</div>
            </div>
            <div class="cust-card-region">India</div>
          </div>
          <div class="cust-card-body">
            <div class="cust-card-sector" style="color:#2E4DEA;">Government</div>
            <div class="cust-card-name">State of Manipur</div>
            <div class="cust-card-loc">Manipur · India</div>
            <div class="cust-card-blurb">Partnering with Cognecto to digitally transform state-wide infrastructure projects with advanced monitoring and AI.</div>
            <div class="cust-card-cta">Read case study &rarr;</div>
          </div>
        </a>"""

# find BRO card end and insert
content = content.replace('</a>\n        <a href="wcl.html" class="cust-card" data-tags="mining industrial" data-region="india">', manipur_card + '\n        <a href="wcl.html" class="cust-card" data-tags="mining industrial" data-region="india">')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated customers/index.html with Manipur customer card')
