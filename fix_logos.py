import re
import base64

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Encode new images
img1_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779437502441.jpg'
img2_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779437636313.jpg'

b64_bro = base64.b64encode(open(img2_path, 'rb').read()).decode('utf-8')
b64_manipur = base64.b64encode(open(img1_path, 'rb').read()).decode('utf-8')

bro_block = re.search(r'"bro": \{[^}]*\}', content, re.DOTALL)
if bro_block:
    new_bro = '"bro": {\n    src: "data:image/jpeg;base64,' + b64_bro + '",\n    alt: "BRO",\n    bg: "#ffffff"\n  }'
    content = content.replace(bro_block.group(0), new_bro)

manipur_block = re.search(r'"manipur": \{[^}]*\}', content, re.DOTALL)
if manipur_block:
    new_manipur = '"manipur": {\n    src: "data:image/jpeg;base64,' + b64_manipur + '",\n    alt: "State of Manipur",\n    bg: "#ffffff"\n  }'
    content = content.replace(manipur_block.group(0), new_manipur)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with correct logos')
