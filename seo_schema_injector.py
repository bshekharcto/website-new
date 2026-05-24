"""
SEO Schema Injector for Cognecto
Injects FAQ Schema, BreadcrumbList, Article Schema, and Product Schema
into all HTML pages across the site.
"""
import os
import json
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"

# ============================================================
# SCHEMA DEFINITIONS
# ============================================================

ORG_SCHEMA = {
    "@type": "Organization",
    "name": "Cognecto",
    "url": "https://cognecto.com/",
    "logo": "https://cognecto.com/favicon.svg"
}

def breadcrumb_schema(items):
    """items = [("Home", "https://cognecto.com/"), ("Solutions", "..."), ("Mining", "...")]"""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": url
            }
            for i, (name, url) in enumerate(items)
        ]
    }

def faq_schema(qa_pairs):
    """qa_pairs = [("question", "answer"), ...]"""
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            }
            for q, a in qa_pairs
        ]
    }

def article_schema(title, description, url, image, date="2026-05-24"):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "url": url,
        "image": image,
        "datePublished": date,
        "dateModified": date,
        "author": ORG_SCHEMA,
        "publisher": ORG_SCHEMA
    }

def software_schema(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": name,
        "description": desc,
        "url": url,
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Cloud",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "INR",
            "availability": "https://schema.org/OnlineOnly"
        },
        "provider": ORG_SCHEMA
    }

def webpage_schema(name, desc, url):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "description": desc,
        "url": url,
        "isPartOf": {
            "@type": "WebSite",
            "name": "Cognecto",
            "url": "https://cognecto.com/"
        }
    }

# ============================================================
# PAGE-SPECIFIC SCHEMAS
# ============================================================

SOLUTION_PAGES = {
    "pages/solutions/highway.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Solutions", "https://cognecto.com/"), ("Highway Construction", "https://cognecto.com/pages/solutions/highway.html")],
        "faq": [
            ("What is Cognecto's highway construction monitoring platform?", "Cognecto provides an end-to-end AI platform for highway and road construction, covering pre-construction baseline surveys, real-time construction monitoring with IoT sensors, and post-construction condition assessment. It is actively used across PMGSY, NHAI, and state highway programmes in India."),
            ("How does AI monitor road compaction in real time?", "Cognecto's Boson Listener IoT sensors are installed on compaction rollers to capture vibration, GPS coordinates, and pass counts in real time. The data is streamed to the Cortex dashboard where AI algorithms automatically verify compaction quality against MORTH specifications."),
            ("What is PMGSY road monitoring and how does Cognecto help?", "PMGSY (Pradhan Mantri Gram Sadak Yojana) is India's rural road construction programme. Cognecto provides OMMAS-integrated monitoring with camera telemetry, automated BOQ verification, and milestone tracking to ensure quality and transparency across thousands of rural road projects."),
            ("How does Cognecto verify Bill of Quantities (BOQ) for highways?", "Cognecto uses computer vision and sensor data to automatically compare actual material usage, layer thickness, and compaction quality against the contracted BOQ specifications. Discrepancies are flagged in real-time on the Cortex dashboard with photographic evidence."),
            ("What government agencies use Cognecto for highway monitoring?", "Cognecto is used by NRIDA (National Rural Infrastructure Development Agency), UPRRDA (Uttar Pradesh Rural Road Development Agency), BRO (Border Roads Organisation), and multiple state PWDs for road construction quality monitoring and project management.")
        ],
        "webpage": ("Highway & Road Construction Intelligence", "Cognecto's end-to-end highway intelligence platform — from pre-construction PMIS and baseline surveys to real-time construction monitoring and post-construction condition assessment.", "https://cognecto.com/pages/solutions/highway.html")
    },
    "pages/solutions/mining.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Solutions", "https://cognecto.com/"), ("Mining", "https://cognecto.com/pages/solutions/mining.html")],
        "faq": [
            ("What is Cognecto's AI platform for open-cast mining?", "Cognecto provides an end-to-end AI and IoT platform for open-cast mines, covering shift planning, haul cycle analytics, fuel management, predictive maintenance, operator attendance, blasting workflows, and a real-time control centre. It is active across WCL, NLC, Hindalco, and FG Gold mining operations."),
            ("How does AI improve mining fleet management?", "Cognecto uses GPS telemetry and vision AI to track every dump truck, excavator, and loader in real time. The platform optimizes haul routes, reduces idle time, monitors fuel consumption per trip, and provides shift-wise productivity reports for mine managers."),
            ("What IoT sensors does Cognecto use in mines?", "Cognecto deploys Boson Listener sensors on heavy mining equipment to capture vibration data, GPS coordinates, engine telemetry, and fuel consumption. Photon Vision cameras monitor safety zones, material loading quality, and operator compliance."),
            ("How does Cognecto ensure mining safety and EHS compliance?", "Cognecto's Photon Vision AI cameras detect PPE violations, unauthorized zone entry, proximity hazards near heavy equipment, and unsafe operator behavior in real time. Alerts are sent to the safety control room within seconds."),
            ("Which mining companies use Cognecto?", "Cognecto is deployed at Western Coalfields Limited (WCL), NLC India Limited, Hindalco Industries, FG Gold Mining, Fura Gems, Canyon Resources, and CAMALCO across India, Australia, Cameroon, and Colombia.")
        ],
        "webpage": ("Open-Cast Mining Intelligence", "End-to-end AI and IoT platform for open-cast mines — shift planning, haul cycle analytics, fuel management, predictive maintenance, operator attendance, blasting workflows, and real-time control centre.", "https://cognecto.com/pages/solutions/mining.html")
    },
    "pages/solutions/water.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Solutions", "https://cognecto.com/"), ("Water Networks", "https://cognecto.com/pages/solutions/water.html")],
        "faq": [
            ("What is Cognecto's smart water network platform?", "Cognecto provides AI-powered monitoring for industrial and municipal water networks, including real-time flow monitoring, pressure analytics, leak detection, non-revenue water (NRW) reduction, and automated billing verification using LoRaWAN IoT sensors."),
            ("How does Cognecto reduce Non-Revenue Water (NRW)?", "Cognecto deploys ultrasonic flow meters and pressure sensors across the water distribution network. AI algorithms analyze flow patterns to detect leaks, unauthorized connections, and meter inaccuracies. Customers like WATCO Odisha have achieved 30%+ NRW reduction."),
            ("What is Jal Jeevan Mission and how does Cognecto support it?", "Jal Jeevan Mission is India's programme to provide piped drinking water to every rural household. Cognecto provides baseline surveys, water quality monitoring, and distribution analytics to support state agencies implementing the mission."),
            ("What IoT technology does Cognecto use for water monitoring?", "Cognecto uses LoRaWAN-based IoT sensors for long-range, low-power water monitoring. Sensors measure flow rate, pressure, water quality (TDS, chlorine, turbidity), and tank levels. Data is transmitted wirelessly to the cloud-based Cortex dashboard.")
        ],
        "webpage": ("Smart Water Network Intelligence", "AI-powered monitoring for industrial and municipal water networks — flow monitoring, pressure analytics, leak detection, NRW reduction, and automated billing verification.", "https://cognecto.com/pages/solutions/water.html")
    },
    "pages/solutions/ehs.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Solutions", "https://cognecto.com/"), ("EHS & Safety", "https://cognecto.com/pages/solutions/ehs.html")],
        "faq": [
            ("What is Cognecto's EHS and industrial safety platform?", "Cognecto's EHS platform uses Photon Vision AI cameras to monitor worksite safety in real time. It detects PPE violations, restricted zone breaches, unsafe equipment operation, and near-miss incidents, generating automated alerts and compliance reports."),
            ("How does Vision AI improve workplace safety?", "Cognecto's AI models analyze live camera feeds to detect safety hazards like missing helmets, harnesses, or reflective vests, personnel in danger zones near heavy equipment, and improper material handling. Violations trigger instant alerts to safety officers."),
            ("What industries use Cognecto for EHS monitoring?", "Cognecto's EHS platform is used in open-cast mining, highway construction sites, industrial plants, and water infrastructure projects. Any site with heavy machinery and manual labor benefits from automated safety monitoring."),
            ("How does Cognecto generate safety compliance reports?", "Cognecto automatically logs every safety event with timestamp, location, camera footage, and violation type. Daily, weekly, and monthly safety reports are generated on the Cortex dashboard, ready for regulatory submission and audit purposes.")
        ],
        "webpage": ("EHS & Industrial Safety Intelligence", "AI-powered workplace safety monitoring using vision AI — PPE detection, restricted zone monitoring, incident tracking, and automated compliance reporting.", "https://cognecto.com/pages/solutions/ehs.html")
    }
}

PLATFORM_PAGES = {
    "pages/platform/boson.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Platform", "https://cognecto.com/"), ("Boson Listener", "https://cognecto.com/pages/platform/boson.html")],
        "faq": [
            ("What is Boson Listener?", "Boson Listener is Cognecto's edge IoT hardware platform that captures real-time telemetry from heavy infrastructure equipment. It measures vibration, GPS position, engine parameters, and environmental conditions, streaming data to the cloud for AI analysis."),
            ("What sensors does Boson Listener use?", "Boson Listener integrates accelerometers for vibration and compaction monitoring, GPS modules for location tracking, fuel flow sensors, temperature and humidity sensors, and CAN bus interfaces for engine telemetry on heavy equipment."),
            ("How is Boson Listener installed on equipment?", "Boson Listener is a ruggedized, IP67-rated device designed for harsh industrial environments. It is magnetically mounted or bolted onto compaction rollers, dump trucks, excavators, and other heavy equipment. Installation takes under 30 minutes per unit."),
            ("What data does Boson Listener transmit?", "Boson Listener transmits vibration amplitude, frequency, GPS coordinates, speed, fuel consumption rate, engine RPM, and operating hours. Data is streamed in real time via 4G/LTE or stored locally and synced via WiFi at the site office.")
        ],
        "software": ("Boson Listener", "Edge IoT hardware platform for real-time telemetry capture from heavy infrastructure equipment — vibration, GPS, fuel, and engine monitoring.", "https://cognecto.com/pages/platform/boson.html")
    },
    "pages/platform/photon.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Platform", "https://cognecto.com/"), ("Photon Vision", "https://cognecto.com/pages/platform/photon.html")],
        "faq": [
            ("What is Photon Vision?", "Photon Vision is Cognecto's computer vision AI platform that processes live camera feeds from infrastructure sites. It uses deep learning models to detect safety violations, monitor material quality, verify construction progress, and track equipment utilization."),
            ("How does Photon Vision detect safety violations?", "Photon Vision AI models are trained to identify PPE non-compliance (missing helmets, vests, harnesses), unauthorized personnel in restricted zones, proximity hazards near heavy equipment, and unsafe material handling practices from standard CCTV camera feeds."),
            ("What cameras work with Photon Vision?", "Photon Vision works with any IP camera or CCTV system. It supports RTSP, ONVIF, and HTTP streaming protocols. Existing site cameras can be connected without additional hardware, or Cognecto can deploy ruggedized cameras for harsh environments."),
            ("How accurate is Photon Vision's AI detection?", "Photon Vision achieves 95%+ accuracy on PPE detection and 92%+ on equipment classification in field conditions. Models are continuously retrained on site-specific data to improve accuracy for each deployment's unique environment and equipment types.")
        ],
        "software": ("Photon Vision", "Computer vision AI platform for infrastructure monitoring — safety violation detection, material quality verification, construction progress tracking, and equipment utilization analysis.", "https://cognecto.com/pages/platform/photon.html")
    },
    "pages/platform/cortex.html": {
        "breadcrumb": [("Home", "https://cognecto.com/"), ("Platform", "https://cognecto.com/"), ("Cortex", "https://cognecto.com/pages/platform/cortex.html")],
        "faq": [
            ("What is Cortex?", "Cortex is Cognecto's AI-powered command and control dashboard that aggregates data from Boson Listener sensors and Photon Vision cameras into a unified operational view. It provides real-time KPIs, alerts, reports, and predictive analytics for infrastructure projects."),
            ("What can you monitor on the Cortex dashboard?", "Cortex provides real-time monitoring of construction progress, equipment utilization, safety compliance, material consumption, BOQ verification, milestone tracking, maintenance schedules, and environmental conditions — all from a single dashboard."),
            ("How does Cortex generate reports?", "Cortex automatically generates daily, weekly, and monthly reports covering project progress, equipment productivity, safety incidents, material reconciliation, and financial summaries. Reports can be exported as PDF, Excel, or shared via automated email schedules."),
            ("Can Cortex integrate with government systems like OMMAS?", "Yes, Cortex provides API integrations with government project management systems like OMMAS (Online Management, Monitoring and Accounting System) for PMGSY, state PWD systems, and other e-governance platforms for automated progress reporting.")
        ],
        "software": ("Cortex", "AI-powered command and control dashboard for infrastructure monitoring — real-time KPIs, alerts, reports, and predictive analytics aggregating data from IoT sensors and vision AI.", "https://cognecto.com/pages/platform/cortex.html")
    }
}

# Resource pages — extract title and description from existing meta tags
RESOURCE_PAGES = [
    "pages/resources/blog-future-of-infra.html",
    "pages/resources/blog-jal-jeevan-baseline.html",
    "pages/resources/blog-vision-ai-mining.html",
    "pages/resources/boq-verification-architecture.html",
    "pages/resources/boson-product-brief.html",
    "pages/resources/fura-gems-multi-continent.html",
    "pages/resources/mining-platform-brief.html",
    "pages/resources/photon-product-brief.html",
    "pages/resources/physics-ai-vs-cv.html",
    "pages/resources/smart-water-loRaWAN.html",
    "pages/resources/video-mining-tour.html",
    "pages/resources/watco-odisha-nrw.html",
    "pages/resources/webinar-nrw-strategies.html",
    "pages/resources/webinar-pmgsy-evidence.html",
]

CUSTOMER_PAGES = [
    "pages/customers/beml.html",
    "pages/customers/bro.html",
    "pages/customers/camalco.html",
    "pages/customers/canyon.html",
    "pages/customers/fg-gold.html",
    "pages/customers/fura-gems.html",
    "pages/customers/hindalco.html",
    "pages/customers/ion-exchange.html",
    "pages/customers/jal-jeevan.html",
    "pages/customers/nlc.html",
    "pages/customers/nrida.html",
    "pages/customers/uprrda-case-study.html",
    "pages/customers/uprrda.html",
    "pages/customers/watco.html",
    "pages/customers/wcl.html",
]

# ============================================================
# INJECTION LOGIC
# ============================================================

def extract_meta(html, attr):
    """Extract content from a meta tag."""
    pattern = rf'<meta\s+(?:name|property)="{attr}"\s+content="([^"]*)"'
    m = re.search(pattern, html)
    if m:
        return m.group(1)
    # Try reversed attribute order
    pattern2 = rf'content="([^"]*)"\s*/?\s*>\s*$'
    return ""

def extract_title(html):
    m = re.search(r'<title>([^<]*)</title>', html)
    return m.group(1) if m else ""

def extract_og(html, prop):
    pattern = rf'property="og:{prop}"\s+content="([^"]*)"'
    m = re.search(pattern, html)
    if m:
        return m.group(1)
    pattern2 = rf'content="([^"]*)"\s*.*?property="og:{prop}"'
    m2 = re.search(pattern2, html)
    return m2.group(1) if m2 else ""

def inject_schema(filepath, schemas):
    """Inject JSON-LD schema(s) before </head>."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Build the script tags
    script_tags = []
    for schema in schemas:
        script_tags.append(f'  <script type="application/ld+json">\n  {json.dumps(schema, indent=2, ensure_ascii=False)}\n  </script>')
    
    injection = '\n'.join(script_tags) + '\n'
    
    # Remove any existing non-home JSON-LD (to avoid duplicates on re-run)
    # Only remove schemas we're about to re-inject
    html = re.sub(r'\s*<script type="application/ld\+json">\s*\{[^}]*"@type"\s*:\s*"(FAQPage|BreadcrumbList|Article|SoftwareApplication|WebPage)"[^<]*</script>', '', html)
    
    # Inject before </head>
    if '</head>' in html:
        html = html.replace('</head>', injection + '</head>', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

def process_solution_pages():
    for rel_path, config in SOLUTION_PAGES.items():
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            continue
        
        schemas = []
        schemas.append(breadcrumb_schema(config["breadcrumb"]))
        schemas.append(faq_schema(config["faq"]))
        schemas.append(webpage_schema(*config["webpage"]))
        
        inject_schema(filepath, schemas)
        print(f"  ✓ {rel_path} — BreadcrumbList + FAQPage + WebPage")

def process_platform_pages():
    for rel_path, config in PLATFORM_PAGES.items():
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            continue
        
        schemas = []
        schemas.append(breadcrumb_schema(config["breadcrumb"]))
        schemas.append(faq_schema(config["faq"]))
        schemas.append(software_schema(*config["software"]))
        
        inject_schema(filepath, schemas)
        print(f"  ✓ {rel_path} — BreadcrumbList + FAQPage + SoftwareApplication")

def process_resource_pages():
    for rel_path in RESOURCE_PAGES:
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        title = extract_title(html)
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html)
        desc = desc_match.group(1) if desc_match else title
        url = f"https://cognecto.com/{rel_path}"
        image_match = re.search(r'property="og:image"\s+content="([^"]*)"', html)
        image = image_match.group(1) if image_match else "https://cognecto.com/favicon.svg"
        
        # Clean title for resource name
        clean_title = title.replace(" | Cognecto Resources", "").replace(" | Cognecto", "")
        
        schemas = []
        bc = [("Home", "https://cognecto.com/"), ("Resources", "https://cognecto.com/pages/resources/index.html"), (clean_title[:60], url)]
        schemas.append(breadcrumb_schema(bc))
        schemas.append(article_schema(title, desc, url, image))
        
        inject_schema(filepath, schemas)
        print(f"  ✓ {rel_path} — BreadcrumbList + Article")

def process_customer_pages():
    for rel_path in CUSTOMER_PAGES:
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            print(f"  SKIP (not found): {rel_path}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        title = extract_title(html)
        desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html)
        desc = desc_match.group(1) if desc_match else title
        url = f"https://cognecto.com/{rel_path}"
        image_match = re.search(r'property="og:image"\s+content="([^"]*)"', html)
        image = image_match.group(1) if image_match else "https://cognecto.com/favicon.svg"
        
        clean_title = title.replace(" | Cognecto", "").replace(" — Cognecto", "")
        
        schemas = []
        bc = [("Home", "https://cognecto.com/"), ("Customers", "https://cognecto.com/pages/customers/index.html"), (clean_title[:60], url)]
        schemas.append(breadcrumb_schema(bc))
        schemas.append(article_schema(title, desc, url, image))
        
        inject_schema(filepath, schemas)
        print(f"  ✓ {rel_path} — BreadcrumbList + Article")


if __name__ == "__main__":
    print("=" * 60)
    print("Cognecto SEO Schema Injector")
    print("=" * 60)
    
    print("\n[1/4] Processing Solution Pages...")
    process_solution_pages()
    
    print("\n[2/4] Processing Platform Pages...")
    process_platform_pages()
    
    print("\n[3/4] Processing Resource Pages...")
    process_resource_pages()
    
    print("\n[4/4] Processing Customer Pages...")
    process_customer_pages()
    
    print("\n" + "=" * 60)
    print("Done! All schemas injected successfully.")
    print("=" * 60)
