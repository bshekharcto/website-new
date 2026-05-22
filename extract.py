with open('pages/platform/photon.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('class="hero-screen-section"')
if idx != -1:
    with open('hero_html.txt', 'w', encoding='utf-8') as f:
        f.write(content[idx:idx+3000])
