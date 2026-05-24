import os
import re

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
updates = {
    "index.html": "Cognecto is the AI operating system for physical infrastructure. Track compaction, material flow, quality, and EHS dynamically with IoT and vision AI.",
    "pages/solutions/highway.html": "AI-powered monitoring for highway construction. Track roller compaction, material flow, and defect detection in real-time. Active on NHAI and PMGSY sites.",
    "pages/solutions/mining.html": "End-to-end AI platform for open-cast mines. Automate shift planning, haul cycle analytics, fuel management, and EHS workflows across your HEMM fleet.",
    "pages/solutions/water.html": "Smart water intelligence platform. End-to-end ultrasonic AMR meters (NB-IoT/LoRaWAN), NRW leak analytics, SCADA integration, and consumer billing apps.",
    "pages/solutions/ehs.html": "Industrial EHS monitoring via vision AI. Automate PPE compliance tracking, intrusion alerts, and fire/smoke detection for secure heavy infrastructure sites.",
    "pages/platform/boson.html": "Boson is the field-intelligence layer that hears your machinery. Use IoT sensors and physics AI to track roller passes, asset health, and field deviations.",
    "pages/platform/photon.html": "Photon is the visual-intelligence layer that sees your worksite. Edge AI runs 24/7 on CCTV cameras to detect PPE violations and early hazard signatures.",
    "pages/platform/cortex.html": "Cortex is the decision-intelligence layer. A real-time control room unifying field data, verifying BOQ compliance, and automating shift production logs."
}

for rel_path, new_desc in updates.items():
    filepath = os.path.join(BASE_DIR, rel_path)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # We find and replace the content inside the meta description tag
        def repl(m):
            # m.group(0) is the full match
            full = m.group(0)
            old_content = m.group(1)
            return full.replace(f'"{old_content}"', f'"{new_desc}"')
            
        new_html = re.sub(r'<meta\s+name="description"\s+content="([^"]*)"\s*>', repl, html, flags=re.IGNORECASE)
        # handle reverse order
        new_html = re.sub(r'<meta\s+content="([^"]*)"\s+name="description"\s*>', repl, new_html, flags=re.IGNORECASE)
        
        # Some pages only had 'Cognecto' and didn't match the standard quotes maybe?
        if new_html == html:
            # Let's just do a brute force regex replace
            new_html = re.sub(r'<meta[^>]+name="description"[^>]*>', f'<meta name="description" content="{new_desc}">', html, flags=re.IGNORECASE)
            
            if new_html == html:
                new_html = re.sub(r'<meta[^>]+content="[^"]*"[^>]*name="description"[^>]*>', f'<meta name="description" content="{new_desc}">', html, flags=re.IGNORECASE)
        
        if new_html != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Updated {rel_path} to {len(new_desc)} chars")
        else:
            print(f"Failed to update {rel_path}")
    else:
        print(f"File not found: {filepath}")
