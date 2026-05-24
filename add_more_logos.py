import base64
import re

img1_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779430754953.jpg'
img2_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779430754958.jpg'

try:
    b64_bro = base64.b64encode(open(img1_path, 'rb').read()).decode('utf-8')
    b64_manipur = base64.b64encode(open(img2_path, 'rb').read()).decode('utf-8')
except Exception as e:
    print('Error reading images:', e)
    exit(1)

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

logos_insertion = f""",
  "bro": {{
    src: "data:image/jpeg;base64,{b64_bro}",
    alt: "BRO",
    bg: "#ffffff"
  }},
  "manipur": {{
    src: "data:image/jpeg;base64,{b64_manipur}",
    alt: "State of Manipur",
    bg: "#ffffff"
  }}
}};
</script>"""

content = re.sub(r'};\s*</script>', logos_insertion, content, count=1)

tiles_insertion = r'<div class="ls-tile" data-logo="excelsource"></div>\n      <div class="ls-tile" data-logo="bro"></div>\n      <div class="ls-tile" data-logo="manipur"></div>'
content = re.sub(r'<div class="ls-tile" data-logo="excelsource"></div>', tiles_insertion, content, count=1)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with bro and manipur logos')
