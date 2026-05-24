import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"

# Re-using the FAQ content from Phase 1
FAQ_CONTENT = {
    "pages/solutions/highway.html": [
        ("What is Cognecto's highway construction monitoring platform?", "Cognecto provides an end-to-end AI platform for highway and road construction, covering pre-construction baseline surveys, real-time construction monitoring with IoT sensors, and post-construction condition assessment. It is actively used across PMGSY, NHAI, and state highway programmes in India."),
        ("How does AI monitor road compaction in real time?", "Cognecto's Boson Listener IoT sensors are installed on compaction rollers to capture vibration, GPS coordinates, and pass counts in real time. The data is streamed to the Cortex dashboard where AI algorithms automatically verify compaction quality against MORTH specifications."),
        ("What is PMGSY road monitoring and how does Cognecto help?", "PMGSY (Pradhan Mantri Gram Sadak Yojana) is India's rural road construction programme. Cognecto provides OMMAS-integrated monitoring with camera telemetry, automated BOQ verification, and milestone tracking to ensure quality and transparency across thousands of rural road projects."),
        ("How does Cognecto verify Bill of Quantities (BOQ) for highways?", "Cognecto uses computer vision and sensor data to automatically compare actual material usage, layer thickness, and compaction quality against the contracted BOQ specifications. Discrepancies are flagged in real-time on the Cortex dashboard with photographic evidence."),
        ("What government agencies use Cognecto for highway monitoring?", "Cognecto is used by NRIDA (National Rural Infrastructure Development Agency), UPRRDA (Uttar Pradesh Rural Road Development Agency), BRO (Border Roads Organisation), and multiple state PWDs for road construction quality monitoring and project management.")
    ],
    "pages/solutions/mining.html": [
        ("What is Cognecto's AI platform for open-cast mining?", "Cognecto provides an end-to-end AI and IoT platform for open-cast mines, covering shift planning, haul cycle analytics, fuel management, predictive maintenance, operator attendance, blasting workflows, and a real-time control centre. It is active across WCL, NLC, Hindalco, and FG Gold mining operations."),
        ("How does AI improve mining fleet management?", "Cognecto uses GPS telemetry and vision AI to track every dump truck, excavator, and loader in real time. The platform optimizes haul routes, reduces idle time, monitors fuel consumption per trip, and provides shift-wise productivity reports for mine managers."),
        ("What IoT sensors does Cognecto use in mines?", "Cognecto deploys Boson Listener sensors on heavy mining equipment to capture vibration data, GPS coordinates, engine telemetry, and fuel consumption. Photon Vision cameras monitor safety zones, material loading quality, and operator compliance."),
        ("How does Cognecto ensure mining safety and EHS compliance?", "Cognecto's Photon Vision AI cameras detect PPE violations, unauthorized zone entry, proximity hazards near heavy equipment, and unsafe operator behavior in real time. Alerts are sent to the safety control room within seconds."),
        ("Which mining companies use Cognecto?", "Cognecto is deployed at Western Coalfields Limited (WCL), NLC India Limited, Hindalco Industries, FG Gold Mining, Fura Gems, Canyon Resources, and CAMALCO across India, Australia, Cameroon, and Colombia.")
    ],
    "pages/solutions/water.html": [
        ("What is Cognecto's smart water network platform?", "Cognecto provides AI-powered monitoring for industrial and municipal water networks, including real-time flow monitoring, pressure analytics, leak detection, non-revenue water (NRW) reduction, and automated billing verification using LoRaWAN IoT sensors."),
        ("How does Cognecto reduce Non-Revenue Water (NRW)?", "Cognecto deploys ultrasonic flow meters and pressure sensors across the water distribution network. AI algorithms analyze flow patterns to detect leaks, unauthorized connections, and meter inaccuracies. Customers like WATCO Odisha have achieved 30%+ NRW reduction."),
        ("What is Jal Jeevan Mission and how does Cognecto support it?", "Jal Jeevan Mission is India's programme to provide piped drinking water to every rural household. Cognecto provides baseline surveys, water quality monitoring, and distribution analytics to support state agencies implementing the mission."),
        ("What IoT technology does Cognecto use for water monitoring?", "Cognecto uses LoRaWAN-based IoT sensors for long-range, low-power water monitoring. Sensors measure flow rate, pressure, water quality (TDS, chlorine, turbidity), and tank levels. Data is transmitted wirelessly to the cloud-based Cortex dashboard.")
    ],
    "pages/solutions/ehs.html": [
        ("What is Cognecto's EHS and industrial safety platform?", "Cognecto's EHS platform uses Photon Vision AI cameras to monitor worksite safety in real time. It detects PPE violations, restricted zone breaches, unsafe equipment operation, and near-miss incidents, generating automated alerts and compliance reports."),
        ("How does Vision AI improve workplace safety?", "Cognecto's AI models analyze live camera feeds to detect safety hazards like missing helmets, harnesses, or reflective vests, personnel in danger zones near heavy equipment, and improper material handling. Violations trigger instant alerts to safety officers."),
        ("What industries use Cognecto for EHS monitoring?", "Cognecto's EHS platform is used in open-cast mining, highway construction sites, industrial plants, and water infrastructure projects. Any site with heavy machinery and manual labor benefits from automated safety monitoring."),
        ("How does Cognecto generate safety compliance reports?", "Cognecto automatically logs every safety event with timestamp, location, camera footage, and violation type. Daily, weekly, and monthly safety reports are generated on the Cortex dashboard, ready for regulatory submission and audit purposes.")
    ],
    "pages/platform/boson.html": [
        ("What is Boson Listener?", "Boson Listener is Cognecto's edge IoT hardware platform that captures real-time telemetry from heavy infrastructure equipment. It measures vibration, GPS position, engine parameters, and environmental conditions, streaming data to the cloud for AI analysis."),
        ("What sensors does Boson Listener use?", "Boson Listener integrates accelerometers for vibration and compaction monitoring, GPS modules for location tracking, fuel flow sensors, temperature and humidity sensors, and CAN bus interfaces for engine telemetry on heavy equipment."),
        ("How is Boson Listener installed on equipment?", "Boson Listener is a ruggedized, IP67-rated device designed for harsh industrial environments. It is magnetically mounted or bolted onto compaction rollers, dump trucks, excavators, and other heavy equipment. Installation takes under 30 minutes per unit."),
        ("What data does Boson Listener transmit?", "Boson Listener transmits vibration amplitude, frequency, GPS coordinates, speed, fuel consumption rate, engine RPM, and operating hours. Data is streamed in real time via 4G/LTE or stored locally and synced via WiFi at the site office.")
    ],
    "pages/platform/photon.html": [
        ("What is Photon Vision?", "Photon Vision is Cognecto's computer vision AI platform that processes live camera feeds from infrastructure sites. It uses deep learning models to detect safety violations, monitor material quality, verify construction progress, and track equipment utilization."),
        ("How does Photon Vision detect safety violations?", "Photon Vision AI models are trained to identify PPE non-compliance (missing helmets, vests, harnesses), unauthorized personnel in restricted zones, proximity hazards near heavy equipment, and unsafe material handling practices from standard CCTV camera feeds."),
        ("What cameras work with Photon Vision?", "Photon Vision works with any IP camera or CCTV system. It supports RTSP, ONVIF, and HTTP streaming protocols. Existing site cameras can be connected without additional hardware, or Cognecto can deploy ruggedized cameras for harsh environments."),
        ("How accurate is Photon Vision's AI detection?", "Photon Vision achieves 95%+ accuracy on PPE detection and 92%+ on equipment classification in field conditions. Models are continuously retrained on site-specific data to improve accuracy for each deployment's unique environment and equipment types.")
    ],
    "pages/platform/cortex.html": [
        ("What is Cortex?", "Cortex is Cognecto's AI-powered command and control dashboard that aggregates data from Boson Listener sensors and Photon Vision cameras into a unified operational view. It provides real-time KPIs, alerts, reports, and predictive analytics for infrastructure projects."),
        ("What can you monitor on the Cortex dashboard?", "Cortex provides real-time monitoring of construction progress, equipment utilization, safety compliance, material consumption, BOQ verification, milestone tracking, maintenance schedules, and environmental conditions — all from a single dashboard."),
        ("How does Cortex generate reports?", "Cortex automatically generates daily, weekly, and monthly reports covering project progress, equipment productivity, safety incidents, material reconciliation, and financial summaries. Reports can be exported as PDF, Excel, or shared via automated email schedules."),
        ("Can Cortex integrate with government systems like OMMAS?", "Yes, Cortex provides API integrations with government project management systems like OMMAS (Online Management, Monitoring and Accounting System) for PMGSY, state PWD systems, and other e-governance platforms for automated progress reporting.")
    ]
}

ALT_TEXT_UPDATES = {
    "pages/solutions/mining.html": {
        'alt="Mining operations control centre"': 'alt="Cognecto Cortex real-time AI dashboard for mining operations control centre"',
        'alt="Open-cast mine haul trucks production"': 'alt="Cognecto AI monitoring haul cycle efficiency for open-cast mine dump trucks"',
        'alt="Mining control centre operations"': 'alt="Aerial view of open-cast mine monitored by Cognecto AI platform"',
        'alt="WCL open-cast coal mine"': 'alt="Cognecto Boson sensors deployed on bulldozers at WCL open-cast coal mine"',
        'alt="NLC lignite mine operations"': 'alt="NLC India lignite mine utilizing Cognecto shift planning and telemetry"',
        'alt="Hindalco aluminium mining plant"': 'alt="Hindalco aluminium mine excavator tracked by Cognecto AI telemetry"',
        'alt="FG Gold open-cast mining West Africa"': 'alt="FG Gold mine dump trucks monitored by Cognecto in West Africa"'
    },
    "pages/solutions/highway.html": {
        'alt="Highway construction quality monitoring"': 'alt="Cognecto AI monitoring highway compaction quality in real time"',
        'alt="Highway construction site monitoring"': 'alt="Cortex dashboard showing PMGSY rural road construction progress"',
        'alt="UPRRDA rural road construction"': 'alt="UPRRDA rural road construction verified by Cognecto BOQ automation"',
        'alt="NRIDA PMGSY road construction"': 'alt="NRIDA PMGSY highway project monitored with Boson compaction sensors"',
        'alt="BRO border roads construction"': 'alt="Border Roads Organisation (BRO) highway construction tracked by Cognecto"'
    },
    "pages/solutions/water.html": {
        'alt="Water treatment plant control room"': 'alt="Cognecto AI dashboard monitoring water flow and NRW analytics"',
        'alt="Water network pressure monitoring"': 'alt="LoRaWAN IoT sensors monitoring water network pressure for Jal Jeevan Mission"',
        'alt="Smart water metering installation"': 'alt="Smart water metering installation tracked by Cognecto Cortex platform"',
        'alt="WATCO Odisha water network"': 'alt="WATCO Odisha water distribution network monitored by Cognecto AI"',
        'alt="Jal Jeevan Mission baseline survey"': 'alt="Jal Jeevan Mission rural water baseline survey using Cognecto platform"'
    },
    "pages/solutions/ehs.html": {
        'alt="Industrial safety monitoring"': 'alt="Cognecto Photon Vision AI detecting PPE compliance in industrial plant"',
        'alt="Construction site safety compliance"': 'alt="Vision AI cameras monitoring construction site safety and hard hat usage"',
        'alt="Mining site hazard detection"': 'alt="Automated proximity hazard detection near heavy mining equipment via AI"',
        'alt="Safety incident reporting dashboard"': 'alt="Cognecto Cortex EHS dashboard showing real-time safety incident reports"'
    },
    "pages/platform/boson.html": {
        'alt="Boson Listener IoT device"': 'alt="Cognecto Boson Listener ruggedized edge IoT device for equipment telemetry"',
        'alt="Vibration sensor installation"': 'alt="Boson Listener vibration and GPS sensor installed on construction equipment"',
        'alt="IoT sensor data transmission"': 'alt="Boson Listener transmitting real-time telematics via 4G LTE to Cortex cloud"'
    },
    "pages/platform/photon.html": {
        'alt="Photon Vision AI cameras"': 'alt="Cognecto Photon Vision AI analyzing live CCTV feeds for safety compliance"',
        'alt="Computer vision object detection"': 'alt="Photon Vision AI object detection recognizing dump trucks and excavators"',
        'alt="AI material volume estimation"': 'alt="Vision AI estimating material volume and payload on mining haul trucks"'
    },
    "pages/platform/cortex.html": {
        'alt="Cortex AI dashboard interface"': 'alt="Cognecto Cortex AI command and control dashboard showing real-time KPIs"',
        'alt="Real-time map and telemetry"': 'alt="Cortex dashboard map view tracking live equipment locations and status"',
        'alt="Automated reporting module"': 'alt="Cortex automated reporting module generating daily BOQ and safety reports"'
    }
}

FAQ_CSS = """
/* ===== FAQ ACCORDION ===== */
.faq-section { background: var(--bg); padding: clamp(4rem, 8vw, 6rem) 0; }
.faq-wrap { max-width: 800px; margin: 0 auto; padding: 0 var(--g); }
.faq-header { text-align: center; margin-bottom: 3rem; }
.faq-title { font-family: var(--display); font-size: clamp(2rem, 3.5vw, 2.5rem); font-weight: 800; color: var(--ink); margin-bottom: 1rem; letter-spacing: -0.03em; }
.faq-subtitle { font-family: var(--body); font-size: 1.1rem; color: var(--ink-3); }
.faq-list { display: flex; flex-direction: column; gap: 1rem; }
.faq-item { border: 1px solid var(--rule); border-radius: 10px; background: white; overflow: hidden; transition: box-shadow 0.2s; }
.faq-item:hover { box-shadow: 0 4px 12px rgba(14,27,53,0.05); }
.faq-question { width: 100%; text-align: left; padding: 1.25rem 1.5rem; display: flex; align-items: center; justify-content: space-between; font-family: var(--display); font-size: 1.1rem; font-weight: 700; color: var(--ink); cursor: pointer; transition: color 0.2s; }
.faq-question:hover { color: var(--blue); }
.faq-icon { width: 24px; height: 24px; display: grid; place-items: center; border-radius: 50%; background: var(--bg-hi); color: var(--blue); transition: transform 0.3s; flex-shrink: 0; }
.faq-item.active .faq-icon { transform: rotate(180deg); background: var(--blue); color: white; }
.faq-answer { padding: 0 1.5rem; max-height: 0; overflow: hidden; transition: all 0.3s ease-in-out; opacity: 0; }
.faq-item.active .faq-answer { padding: 0 1.5rem 1.25rem; max-height: 500px; opacity: 1; }
.faq-answer p { font-family: var(--body); font-size: 1rem; color: var(--ink-2); line-height: 1.6; margin: 0; }
"""

FAQ_JS = """
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
      const btn = item.querySelector('.faq-question');
      btn.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      });
    });
  });
</script>
"""

def generate_faq_html(qa_pairs):
    html = ['<section class="faq-section" id="faq">', '  <div class="faq-wrap">', '    <div class="faq-header">', '      <h2 class="faq-title">Frequently Asked Questions</h2>', '      <p class="faq-subtitle">Find answers to common questions about our platform and deployments.</p>', '    </div>', '    <div class="faq-list">']
    for i, (q, a) in enumerate(qa_pairs):
        active = " active" if i == 0 else ""
        html.append(f'      <div class="faq-item{active}">')
        html.append(f'        <button class="faq-question"><span>{q}</span><div class="faq-icon">↓</div></button>')
        html.append(f'        <div class="faq-answer"><p>{a}</p></div>')
        html.append(f'      </div>')
    html.append('    </div>')
    html.append('  </div>')
    html.append('</section>')
    html.append(FAQ_JS)
    return '\n'.join(html)

def update_page(filepath, faqs, alt_updates):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Alt Texts
    if alt_updates:
        for old, new in alt_updates.items():
            html = html.replace(old, new)

    # 2. Add Semantic <main> tags
    # Find the hero section, which is typically where main content starts
    # Some pages use <section class="hero">, others might use something else
    # We will look for <section class="hero"> or the first <section> after nav
    if '<main role="main">' not in html:
        hero_idx = html.find('<section class="hero">')
        if hero_idx == -1:
            hero_idx = html.find('<section ')
            
        footer_idx = html.find('<footer')
        
        if hero_idx != -1 and footer_idx != -1 and hero_idx < footer_idx:
            html = html[:hero_idx] + '<main role="main">\n' + html[hero_idx:footer_idx] + '</main>\n' + html[footer_idx:]

    # 3. Add FAQ CSS
    if '/* ===== FAQ ACCORDION ===== */' not in html:
        style_end = html.find('</style>')
        if style_end != -1:
            html = html[:style_end] + FAQ_CSS + '\n' + html[style_end:]

    # 4. Add FAQ HTML
    if '<section class="faq-section"' not in html:
        footer_idx = html.find('<footer')
        main_end = html.find('</main>')
        
        insert_idx = main_end if main_end != -1 else footer_idx
        
        if insert_idx != -1:
            faq_html = generate_faq_html(faqs) + '\n\n'
            html = html[:insert_idx] + faq_html + html[insert_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    for rel_path, faqs in FAQ_CONTENT.items():
        filepath = os.path.join(BASE_DIR, rel_path)
        if os.path.exists(filepath):
            alt_updates = ALT_TEXT_UPDATES.get(rel_path, {})
            update_page(filepath, faqs, alt_updates)
        else:
            print(f"Not found: {filepath}")
    
    # Let's also do index.html alt texts and semantic main
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            idx_html = f.read()
        
        # Add semantic <main> if not there
        if '<main role="main">' not in idx_html:
            hero_idx = idx_html.find('<section class="hero">')
            footer_idx = idx_html.find('<footer')
            if hero_idx != -1 and footer_idx != -1 and hero_idx < footer_idx:
                idx_html = idx_html[:hero_idx] + '<main role="main">\n' + idx_html[hero_idx:footer_idx] + '</main>\n' + idx_html[footer_idx:]
        
        # Update some alt texts on index
        idx_alts = {
            'alt="Mining operations"': 'alt="Cognecto AI monitoring open-cast mining operations"',
            'alt="Highway construction"': 'alt="Cognecto tracking real-time PMGSY highway construction compaction"',
            'alt="Water networks"': 'alt="Smart water network leak detection using LoRaWAN IoT sensors"',
            'alt="Industrial safety"': 'alt="Vision AI detecting PPE compliance for industrial safety"'
        }
        for old, new in idx_alts.items():
            idx_html = idx_html.replace(old, new)
            
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(idx_html)
        print(f"Updated index.html")
