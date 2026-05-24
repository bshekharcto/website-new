with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('data-type="company-verification" data-sector="all"', 'data-type="company" data-sector="all"')

new_pill = '<button class="res-filter-pill" data-filter="company">Company</button>'
content = content.replace('<button class="res-filter-pill" data-filter="blog">Blog &amp; Insights</button>', 
                          '<button class="res-filter-pill" data-filter="blog">Blog &amp; Insights</button>\n          ' + new_pill)

with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
