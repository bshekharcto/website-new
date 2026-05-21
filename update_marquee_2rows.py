import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
old_css = """.ls-marquee-wrapper { overflow: hidden; position: relative; width: 100%; display: flex; padding: 10px 0; }
.ls-marquee-wrapper::before, .ls-marquee-wrapper::after { content: ""; position: absolute; top: 0; width: 150px; height: 100%; z-index: 2; pointer-events: none; }
.ls-marquee-wrapper::before { left: 0; background: linear-gradient(to right, var(--bg) 0%, transparent 100%); }
.ls-marquee-wrapper::after { right: 0; background: linear-gradient(to left, var(--bg) 0%, transparent 100%); }
.ls-grid { display: flex; gap: 0.8rem; width: max-content; animation: marquee-scroll 50s linear infinite; }
.ls-grid:hover { animation-play-state: paused; }
@keyframes marquee-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.ls-tile { height: 60px; min-width: 170px; background: white; border: 0.5px solid var(--rule); border-radius: 10px; display: flex; align-items: center; justify-content: center; padding: 0 1rem; transition: border-color 0.15s, box-shadow 0.15s; }
.ls-tile:hover { border-color: var(--rule-2); box-shadow: 0 2px 10px rgba(14,27,53,0.07); }"""

new_css = """.ls-marquee-wrapper { overflow: hidden; position: relative; width: 100%; display: flex; flex-direction: column; padding: 10px 0; }
.ls-marquee-wrapper::before, .ls-marquee-wrapper::after { content: ""; position: absolute; top: 0; width: 150px; height: 100%; z-index: 2; pointer-events: none; }
.ls-marquee-wrapper::before { left: 0; background: linear-gradient(to right, var(--bg) 0%, transparent 100%); }
.ls-marquee-wrapper::after { right: 0; background: linear-gradient(to left, var(--bg) 0%, transparent 100%); }
.ls-grid { display: flex; gap: 0.8rem; width: max-content; animation: marquee-scroll 50s linear infinite; }
.ls-grid.reverse { animation-direction: reverse; animation-duration: 55s; }
.ls-grid:hover { animation-play-state: paused; }
@keyframes marquee-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.ls-tile { height: 60px; min-width: 170px; background: white; border: 0.5px solid var(--rule); border-radius: 10px; display: flex; align-items: center; justify-content: center; padding: 0 1rem; transition: border-color 0.15s, box-shadow 0.15s; }
.ls-tile:hover { border-color: var(--rule-2); box-shadow: 0 2px 10px rgba(14,27,53,0.07); }"""

content = content.replace(old_css, new_css)

logos_top = """      <div class="ls-tile" data-logo="ega"></div>
      <div class="ls-tile" data-logo="hindalco"></div>
      <div class="ls-tile" data-logo="metlen"></div>
      <div class="ls-tile" data-logo="thyssenkrupp"></div>
      <div class="ls-tile" data-logo="vedanta"></div>
      <div class="ls-tile" data-logo="coal-india"></div>
      <div class="ls-tile" data-logo="nlc-india"></div>
      <div class="ls-tile" data-logo="watco"></div>
      <div class="ls-tile" data-logo="fura-gems"></div>
      <div class="ls-tile" data-logo="fg-gold"></div>
      <div class="ls-tile" data-logo="camalco"></div>
      <div class="ls-tile" data-logo="beml"></div>
      <div class="ls-tile" data-logo="bhel"></div>
      <div class="ls-tile" data-logo="ministry-rural-development"></div>"""

logos_bottom = """      <div class="ls-tile" data-logo="govt-tripura"></div>
      <div class="ls-tile" data-logo="govt-nagaland"></div>
      <div class="ls-tile" data-logo="govt-kerala"></div>
      <div class="ls-tile" data-logo="govt-mizoram"></div>
      <div class="ls-tile" data-logo="govt-puducherry"></div>
      <div class="ls-tile" data-logo="canyon-resources"></div>
      <div class="ls-tile" data-logo="pmgsy"></div>
      <div class="ls-tile" data-logo="upeida"></div>
      <div class="ls-tile" data-logo="ladakh"></div>
      <div class="ls-tile" data-logo="madhya-pradesh"></div>
      <div class="ls-tile" data-logo="uttar-pradesh"></div>
      <div class="ls-tile" data-logo="a2mp"></div>
      <div class="ls-tile" data-logo="ion-exchange"></div>
      <div class="ls-tile" data-logo="flytta"></div>"""

# Replace HTML by matching from <div class="ls-marquee-wrapper"> to the end of it
html_pattern = re.compile(r'<div class="ls-marquee-wrapper">.*?</div>\n  </div>', re.DOTALL)

new_html = f"""<div class="ls-marquee-wrapper">
    <div class="ls-grid" style="margin-bottom: 0.8rem;">
{logos_top}
{logos_top}
    </div>
    <div class="ls-grid reverse">
{logos_bottom}
{logos_bottom}
    </div>
  </div>"""

content = html_pattern.sub(new_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
