# Cognecto Website

Static HTML/CSS/JS website for [cognecto.com](https://www.cognecto.com).  
No build step required — open `index.html` in a browser or serve with any static host.

---

## Structure

```
cognecto-website/
├── index.html                          # Homepage
├── pages/
│   ├── platform/
│   │   ├── boson.html                  # Boson — IoT Sensing & Physics AI
│   │   ├── photon.html                 # Photon — Vision AI & Infrastructure Intelligence
│   │   └── cortex.html                 # Cortex — Decision Intelligence & Knowledge Graph
│   └── solutions/
│       └── highway.html                # Solution: Highway & Road Construction
├── assets/
│   ├── css/                            # (reserved for extracted stylesheets)
│   ├── js/                             # (reserved for extracted scripts)
│   └── images/                         # (reserved for local image assets)
└── README.md
```

---

## Pages

| File | Route | Description |
|------|-------|-------------|
| `index.html` | `/` | Homepage — full platform overview, logo carousel, customer section |
| `pages/platform/boson.html` | `/platform/boson` | Boson product page — IoT sensing, pass counting, multi-OEM |
| `pages/platform/photon.html` | `/platform/photon` | Photon product page — Vision AI, road construction, mining, safety |
| `pages/platform/cortex.html` | `/platform/cortex` | Cortex product page — Knowledge graph, BOQ verification, co-pilot |
| `pages/solutions/highway.html` | `/solutions/highway` | Highway solution — pre/during/post construction intelligence |

### Pages still to build
- `pages/solutions/mining.html` — Open-cast mining shift planning & fleet intelligence
- `pages/solutions/water.html` — Smart water metering & NRW reduction
- `pages/solutions/smart-cities.html` — Urban infrastructure monitoring

---

## Tech stack

- **Pure HTML + CSS + JavaScript** — no frameworks, no bundler
- **Fonts**: Manrope + Space Grotesk via Google Fonts
- **Images**: Pexels CDN (replace with owned assets before production)
- **Icons**: Inline SVG throughout
- **Logos**: Base64-encoded inline (homepage only — extract to `/assets/images/logos/` for production)

---

## Design tokens

Defined in `:root` on every page:

```css
--blue:    #2E4DEA;   /* Boson / primary UI */
--navy:    #0E1B35;   /* Dark backgrounds, CTAs */
--ink:     #1A2540;   /* Body text */
--green:   #0BA868;   /* Cortex */
--teal:    #0891B2;   /* Photon */
--road:    #D97706;   /* Highway solution */
--display: 'Manrope', sans-serif;
--body:    'Space Grotesk', sans-serif;
```

---

## Developer notes

### Internal linking
All internal `href` values use **relative paths** from the file's location:
- From `index.html` → `pages/platform/boson.html`
- From `pages/platform/*.html` → `../../index.html`, `boson.html`, `cortex.html`
- From `pages/solutions/*.html` → `../../index.html`, `../platform/boson.html`

### Logo base64
The Cognecto nav logo is base64-encoded inline in each product/solution page to ensure it renders without JS dependency. For production, extract to `/assets/images/cognecto-logo.jpg` and update all `src` attributes.

### Mega menu
The nav mega menu is inherited from the homepage CSS and duplicated in each page. For production, extract to a shared `nav.html` partial and include via a templating system or JS fetch.

### Images for production
All section images currently use Pexels CDN URLs. Before launch:
1. Download and compress images to `/assets/images/`
2. Update `src` and `background-image` references
3. Add `width` and `height` attributes for CLS performance

### CSS/JS extraction (recommended before launch)
Each page currently contains all CSS inline in a `<style>` block. Extract shared styles to:
- `/assets/css/base.css` — design tokens, reset, typography, nav
- `/assets/css/components.css` — shared components (metrics, customer section, moats, FAQ)
- `/assets/css/[page].css` — page-specific styles

---

## Running locally

```bash
# Option 1 — Python (no install needed)
python3 -m http.server 8000
# then open http://localhost:8000

# Option 2 — Node
npx serve .

# Option 3 — VS Code
# Install Live Server extension, right-click index.html → Open with Live Server
```

---

## Deployment

The site is static and deploys to any host:

| Platform | Command / Method |
|----------|-----------------|
| **GitHub Pages** | Push to `main`, enable Pages in repo settings → serve from root |
| **Netlify** | Drag & drop the folder, or connect repo — auto-detects static site |
| **Vercel** | `vercel deploy` from project root |
| **AWS S3** | Upload all files, enable static website hosting, set `index.html` as root |

---

## Contact

Cognecto Private Limited  
info@cognecto.com · www.cognecto.com · +91-9997310261
