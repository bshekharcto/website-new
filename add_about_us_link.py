import re

with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

about_us_card = '''        <a href="about-us.html" class="res-card" data-type="company-verification" data-sector="all" data-featured="true">
          <div class="res-card-img">
            <img src="../../assets/images/highway_bro_main.webp" alt="About Cognecto" loading="lazy"/>
            <div class="res-card-img-overlay" style="background:linear-gradient(160deg,rgba(14,27,53,0.2) 0%,#2E4DEA33 100%);"></div>
            <div class="res-card-type-pill" style="background:#2E4DEA;">About Us</div>
          </div>
          <div class="res-card-body">
            <div class="res-card-meta">
              <span class="res-card-sector" style="color:#2E4DEA;">Company</span>
              <span class="res-card-dot">·</span>
              <span class="res-card-time">5 min read</span>
            </div>
            <div class="res-card-title">About Cognecto</div>
            <div class="res-card-blurb">The AI Operating System for Physical Infrastructure. We are an AI-powered connected operations platform built for the sectors that keep civilisations running.</div>
            <div class="res-card-footer">
              <span class="res-card-date">2026</span>
              <span class="res-card-cta">Read →</span>
            </div>
          </div>
        </a>
'''

html = html.replace('<div class="res-grid" id="res-grid">', '<div class="res-grid" id="res-grid">\n' + about_us_card)

with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
