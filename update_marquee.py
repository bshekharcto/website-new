import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS
old_css = """.ls-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 0.6rem; }
@media(max-width:900px){ .ls-grid { grid-template-columns: repeat(4, 1fr); } }
@media(max-width:580px){ .ls-grid { grid-template-columns: repeat(3, 1fr); } }
.ls-tile { height: 60px; background: white; border: 0.5px solid var(--rule); border-radius: 10px; display: flex; align-items: center; justify-content: center; padding: 0 1rem; opacity: 0; transform: translateY(12px); }
.ls-tile.ls-visible { opacity: 1; transform: translateY(0); transition: opacity 0.4s ease, transform 0.4s ease, border-color 0.15s, box-shadow 0.15s; }
.ls-tile.ls-visible:hover { border-color: var(--rule-2); box-shadow: 0 2px 10px rgba(14,27,53,0.07); }"""

new_css = """.ls-marquee-wrapper { overflow: hidden; position: relative; width: 100%; display: flex; padding: 10px 0; }
.ls-marquee-wrapper::before, .ls-marquee-wrapper::after { content: ""; position: absolute; top: 0; width: 150px; height: 100%; z-index: 2; pointer-events: none; }
.ls-marquee-wrapper::before { left: 0; background: linear-gradient(to right, var(--bg) 0%, transparent 100%); }
.ls-marquee-wrapper::after { right: 0; background: linear-gradient(to left, var(--bg) 0%, transparent 100%); }
.ls-grid { display: flex; gap: 0.8rem; width: max-content; animation: marquee-scroll 50s linear infinite; }
.ls-grid:hover { animation-play-state: paused; }
@keyframes marquee-scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
.ls-tile { height: 60px; min-width: 170px; background: white; border: 0.5px solid var(--rule); border-radius: 10px; display: flex; align-items: center; justify-content: center; padding: 0 1rem; transition: border-color 0.15s, box-shadow 0.15s; }
.ls-tile:hover { border-color: var(--rule-2); box-shadow: 0 2px 10px rgba(14,27,53,0.07); }"""

content = content.replace(old_css, new_css)

# Replace HTML
old_html = """<div class="logo-strip">
  <div class="wrap">
    <div class="ls-label">Trusted by operators, governments and enterprises across 10+ 
countries</div>
    <div class="ls-grid" id="ls-track">

      <div class="ls-tile" data-logo="ega"></div>
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
      <div class="ls-tile" data-logo="ministry-rural-development"></div>

      <!-- Row 3 — Government clients -->
      <div class="ls-tile" data-logo="govt-tripura"></div>
      <div class="ls-tile" data-logo="govt-nagaland"></div>
      <div class="ls-tile" data-logo="govt-kerala"></div>
      <div class="ls-tile" data-logo="govt-mizoram"></div>
      <div class="ls-tile" data-logo="govt-puducherry"></div>
      <div class="ls-tile" data-logo="canyon-resources"></div>
      <div class="ls-tile" data-logo="pmgsy"></div>

      <!-- Row 4 — Additional government & industry clients -->
      <div class="ls-tile" data-logo="upeida"></div>
      <div class="ls-tile" data-logo="ladakh"></div>
      <div class="ls-tile" data-logo="madhya-pradesh"></div>
      <div class="ls-tile" data-logo="uttar-pradesh"></div>
      <div class="ls-tile" data-logo="a2mp"></div>
      <div class="ls-tile" data-logo="ion-exchange"></div>
      <div class="ls-tile" data-logo="flytta"></div>

    </div>
  </div>
</div>"""

logos = """      <div class="ls-tile" data-logo="ega"></div>
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
      <div class="ls-tile" data-logo="ministry-rural-development"></div>
      <div class="ls-tile" data-logo="govt-tripura"></div>
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

new_html = f"""<div class="logo-strip">
  <div class="ls-label">Trusted by operators, governments and enterprises across 10+ countries</div>
  <div class="ls-marquee-wrapper">
    <div class="ls-grid" id="ls-track">
{logos}
{logos}
    </div>
  </div>
</div>"""

content = content.replace(old_html, new_html)

# Clean up JS that adds ls-visible since we don't need scroll reveal anymore
js_to_remove = """// Logo strip staggered fade-in on scroll
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var grid = document.getElementById('ls-track');
    if (!grid) return;
    var tiles = grid.querySelectorAll('.ls-tile');
    var triggered = false;

    var observer = new IntersectionObserver(function(entries) {
      if (entries[0].isIntersecting && !triggered) {
        triggered = true;
        tiles.forEach(function(tile, i) {
          setTimeout(function() {
            tile.classList.add('ls-visible');
          }, i * 60);
        });
        observer.disconnect();
      }
    }, { threshold: 0.2 });

    observer.observe(grid);
  });
})();"""
content = content.replace(js_to_remove, "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
