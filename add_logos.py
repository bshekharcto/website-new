import re
import base64

img1_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779430754953.jpg'
img2_path = r'C:\Users\bhanu\.gemini\antigravity-ide\brain\f2031a1d-5db3-482a-86f0-209fb3f9472e\media__1779430754958.jpg'

try:
    b64_viondot = base64.b64encode(open(img1_path, 'rb').read()).decode('utf-8')
    b64_excelsource = base64.b64encode(open(img2_path, 'rb').read()).decode('utf-8')
except Exception as e:
    print("Error reading images:", e)
    exit(1)

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add to window.LOGOS
logos_insertion = f""",
  "viondot": {{
    src: "data:image/jpeg;base64,{b64_viondot}",
    alt: "Viondot Smart Meter",
    bg: "#ffffff"
  }},
  "excelsource": {{
    src: "data:image/jpeg;base64,{b64_excelsource}",
    alt: "Excelsource",
    bg: "#ffffff"
  }}
}};
</script>"""

content = re.sub(r'};\s*</script>', logos_insertion, content, count=1)

# 2. Add ls-tiles
tiles_insertion = r'<div class="ls-tile" data-logo="flytta"></div>\n      <div class="ls-tile" data-logo="viondot"></div>\n      <div class="ls-tile" data-logo="excelsource"></div>'
content = re.sub(r'<div class="ls-tile" data-logo="flytta"></div>', tiles_insertion, content, count=1)

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html with new logos.")
