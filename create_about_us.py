import re

with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\blog-future-of-infra.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Create about-us.html
out_html = html.replace('The future of infrastructure is verifiable.', 'About Cognecto')
out_html = out_html.replace('blog-future-of-infra.html', 'about-us.html')

main_pattern = re.compile(r'<main>.*?</main>', re.DOTALL)

about_main = '''<main>
        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>About Cognecto</div>
          <h2>The AI Operating System for Physical Infrastructure</h2>
          <p>Cognecto is the intelligence layer the physical world has been missing.</p>
          <p>We are an AI-powered connected operations platform built for the sectors that keep civilisations running — roads and expressways, city water networks, and mines that extract the raw materials the world depends on. We have spent years doing one thing: making physical infrastructure measurable, verifiable, and trusted — at scale, in real time, in the hardest operating environments on earth.</p>
          <p>We are not a dashboarding company. We are not a telematics bolt-on. We are a full-stack AI operating system that ingests signals from the physical world, builds operational context, and delivers structured intelligence to every level of an organisation — from a field supervisor's phone to a Ministry secretary's dashboard, in a single unified interface.</p>
          <p>The infrastructure industry has digitised around the edges for decades. Cognecto digitises the core.</p>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Where We Win</div>
          <h2>Roads & Expressways</h2>
          <p>Cognecto monitors <strong>20,000+ kilometres of roads and highways</strong> — including expressway corridors trusted by some of India's largest road asset owners. Our AI replaces subjective inspections with geo-tagged, timestamped, court-admissible evidence for every compaction pass, every layer, every defect. Clients include government bodies under NHAI, UPRRDA, PMGSY, and state PWDs across India, as well as sovereign infrastructure developers in the Gulf.</p>
          <p>The result: −40% rework cost, −60% inspection time, and for the first time, a legal evidence trail that stands up to scrutiny at every level of government accountability.</p>
          <div class="rdp-quote">
            <div class="rdp-quote-body">"Cognecto has set a benchmark for evidence-based quality monitoring in road construction. The AI-verified inspections replaced subjective assessments and gave us court-admissible evidence trails for the first time."</div>
            <div class="rdp-quote-author">CEO, UPRRDA</div>
          </div>
          <br>
          <h2>City Water Networks</h2>
          <p>Water loss is one of the most expensive and invisible problems municipal operators face. Cognecto's continuous AI monitoring layer — deployed across city water distribution networks — detects anomalies, pressure drops, and early-stage pipe failures before they become emergencies. We turn reactive maintenance into planned intervention, and subjective field reporting into verifiable asset health records. Urban water authorities across South Asia trust Cognecto to protect infrastructure that serves millions of people.</p>
          <br>
          <h2>Mining — 10 Countries & Counting</h2>
          <p>Cognecto operates across mines in <strong>10 countries across four continents</strong> — Asia, Australia, Africa, and Europe. The world's largest emerald mine (FURA Gems, Australia) runs entirely on Cognecto technology. Clients include Emirates Global Aluminium (UAE), Vedanta, Aditya Birla Hindalco, NLC India, Coal India subsidiaries, Metlen Energy & Metals (Greece), Canyon Resources and CAMALCO (Cameroon), FG Gold (West Africa), and WATCO (pan-African logistics).</p>
          <p>We manage HEMM fleets, shift planning, fuel accountability, PPE compliance, and mine-site safety — with outcomes that include <strong>2× mining output</strong> and <strong>99.5% fuel accounting accuracy</strong> at active sites.</p>
          <div class="rdp-quote">
            <div class="rdp-quote-body">"Cognecto doubled our mining capacity and achieved 99.5% fuel accounting accuracy."</div>
            <div class="rdp-quote-author">Jacques</div>
            <div class="rdp-quote-role">North Eastern Mining Company, Australia</div>
          </div>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>The Platform</div>
          <h2>Three Layers. One Intelligence.</h2>
          <p>Cognecto is built on three purpose-engineered product layers that work together as a unified AI operating system. No data science team required. Operational in seven days.</p>
          
          <h3>Boson — Hear</h3>
          <p>Physics-based AI trained on the actual mechanics of compaction, material fatigue, and structural degradation — not just visual patterns. Boson counts every roller pass, verifies every equipment sequence, and flags deviation before concrete sets. It is the IoT listening and sensing layer: GPS-IoT fusion, compaction verification, asset health tracking, and field data ingestion across heterogeneous equipment fleets.</p>
          
          <h3>Photon — See</h3>
          <p>Real-time computer vision across thousands of simultaneous camera streams. Photon doesn't review footage after an incident — it prevents the incident. PPE compliance, no-go zone intrusion, fire and smoke detection, defect classification, visibility conditions, and contractor accountability — all in real time, across multi-site, multi-country deployments. Designed for industrial environments where the cost of a miss is a life or a legal liability.</p>

          <h3>Cortex — Act</h3>
          <p>The intelligence and orchestration layer that turns Boson and Photon signals into decisions. BOQ verification triggers billing. Milestone completion gates the next work order. Equipment downtime updates the shift plan automatically. Every Cortex output is structured, timestamped, and audit-ready. This is where data becomes operational intelligence — for governments, enterprises, and investors who need ground truth, not reports.</p>

          <p>Together, these three layers form a data moat that self-widens: over <strong>500 million data assets</strong> ingested, <strong>15,000+ assets</strong> monitored across <strong>145+ asset types</strong> — and every new deployment sharpens every existing model.</p>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Integrations</div>
          <h2>Off-the-Shelf OEM Integration</h2>
          <p>Cognecto works with the equipment your teams already operate. We have built native integrations for the world's leading HEMM and construction equipment manufacturers — no custom engineering, no lengthy onboarding:</p>
          <p><strong>TATA · Caterpillar · Komatsu · Mahindra · JCB · CNH · Daimler · AJAX · HAMM · Hitachi · Bell · Renault Trucks · BEML · Thyssenkrupp</strong></p>
          <p>This is not a compatibility list. These are live, field-tested integrations running on active project sites today. Our API-first architecture means enterprise ERP, SAP, and third-party systems connect in days, not months.</p>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Differentiator</div>
          <h2>Why Cognecto Is Structurally Different</h2>
          <p>Most AI applied to infrastructure is a point solution — a dashboard, a sensor, a report. Cognecto is built differently, at an architectural level that cannot be replicated by a cloud provider adding an infrastructure module or a systems integrator assembling third-party tools.</p>
          <p><strong>Physics-based transfer learning.</strong> Our AI was trained on the physical laws governing infrastructure degradation — fatigue mechanics, compaction dynamics, corrosion chemistry, flow physics. The same model intelligence that monitors a highway corridor transfers directly to a water pipeline or a mine haul road. This took four years to get right.</p>
          <p><strong>A data moat that self-widens.</strong> 20,000+ km of roads monitored. Millions of compaction-pass readings. Defect libraries built from real construction failures across India, Australia, and East Africa. No publicly available dataset comes close — and the gap widens with every project.</p>
          <p><strong>Patent-protected core IP.</strong> Compaction-pass counting via GPS-IoT fusion, AI defect classification from field video, and multi-sensor infrastructure health scoring — all patent-filed. The core intelligence cannot be commoditised.</p>
          <p><strong>Schema lock-in, not vendor lock-in.</strong> Every project monitored by Cognecto produces a structured, queryable event history — chainage-referenced, timestamped, role-segmented. We become the source of truth for billing, audits, and performance tracking. The infrastructure beneath the infrastructure.</p>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Trust</div>
          <h2>Trusted By</h2>
          <p><strong>Expressway & Road Authorities:</strong> NHAI · UPRRDA · Ministry of Rural Development (PMGSY/NRIDA) · RRDA Nagaland · RRDA Tripura · State PWDs · ADNOC (UAE)</p>
          <p><strong>Mining Enterprises:</strong> Emirates Global Aluminium · FURA Gems · Vedanta · Aditya Birla Hindalco · NLC India · Coal India (WCL, CCL, BCCL, ECL) · BEML · Thyssenkrupp Industries India · Metlen Energy & Metals · Canyon Resources · CAMALCO · WATCO · FG Gold · Government of Sikkim</p>
          <p><strong>Industrial & Infrastructure:</strong> BHEL · Ion Exchange India · JSW Group · Govt. of India (Ministry of Rural Development)</p>
          <p><strong>Water Networks:</strong> Urban water authorities across South Asia (city water distribution & pipeline monitoring)</p>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Recognition</div>
          <h2>Industry Recognized Category Leader</h2>
          <ul>
            <li><strong>#1 Mining Tech Startup in India</strong> — Tracxn (2024)</li>
            <li><strong>Top 5 Global Startup for Predictive Analytics</strong> — StartUs Insights</li>
            <li><strong>Top 25 Key Player, Equipment Monitoring — Global</strong> — Industry ARC</li>
            <li><strong>Business Excellence Award</strong> — Vedanta Group (2023–24)</li>
            <li><strong>Most Innovative Startup</strong> — IIT Delhi (2023)</li>
            <li><strong>CII Centre of Excellence</strong> — Confederation of Indian Industry</li>
            <li><strong>Spacecubed Perth Landing Pad</strong> — Australia's gateway accelerator for international deep-tech</li>
            <li><strong>21 Top Startups Bangalore 2024</strong> — BTFS</li>
            <li><strong>Mines Safety Week 2025–26 Participating Organisation</strong> — NLC India / DGMS</li>
            <li><strong>Top 10 Most Recommended Startup</strong> — CIO Insider</li>
            <li><strong>Top Performing Startup</strong> — Vedanta Spark (2023)</li>
          </ul>
        </div>
        
        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Scale</div>
          <h2>The Numbers</h2>
          <div class="rdp-impact-grid">
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">20,000+</div><div class="rdp-impact-card-l">km Roads Monitored</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">10</div><div class="rdp-impact-card-l">Countries</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">500M+</div><div class="rdp-impact-card-l">Data Assets</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">15,000+</div><div class="rdp-impact-card-l">Connected Assets</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">145+</div><div class="rdp-impact-card-l">Asset Types</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">25-30%</div><div class="rdp-impact-card-l">Efficiency Gain</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">7 Days</div><div class="rdp-impact-card-l">Activation Time</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">4×</div><div class="rdp-impact-card-l">Efficiency (UPRRDA)</div></div>
            <div class="rdp-impact-card"><div class="rdp-impact-card-n">2×</div><div class="rdp-impact-card-l">Mining Output (FURA)</div></div>
          </div>
        </div>

        <div class="rdp-section">
          <div class="rdp-section-label"><span class="rdp-section-label-dot"></span>Contact</div>
          <h2>Get in Touch</h2>
          <p><strong>Cognecto Private Limited</strong></p>
          <p>No. 14, Bhattarahalli, Old Madras Road, KR Puram, Bengaluru — 560049, India</p>
          <p><a href="https://www.cognecto.com">www.cognecto.com</a> · <a href="mailto:contactus@cognecto.com">contactus@cognecto.com</a> · +91 99973 10261</p>
          <p><em>Bengaluru, India · Operating across Asia, Australia, Africa, and Europe</em></p>
        </div>
</main>'''

out_html = main_pattern.sub(about_main, out_html)

out_html = out_html.replace('Blog Post · Platform · All Sectors', 'About Us')
out_html = out_html.replace('6 min read <span>·</span> March 2026 <span>·</span> Cognecto Team', 'Company Overview')
out_html = out_html.replace('Why every dollar invested in public infrastructure now demands an audit trail — and how AI is changing what accountability means.', 'The intelligence layer the physical world has been missing.')
out_html = out_html.replace('class="rdp-hero-stat-n">6 min', 'class="rdp-hero-stat-n">10+')
out_html = out_html.replace('class="rdp-hero-stat-l">Read', 'class="rdp-hero-stat-l">Countries')
out_html = out_html.replace('class="rdp-hero-stat-n">Insight', 'class="rdp-hero-stat-n">20k+')
out_html = out_html.replace('class="rdp-hero-stat-l">Industry perspective', 'class="rdp-hero-stat-l">km Monitored')
out_html = out_html.replace('class="rdp-hero-stat-n">Trust', 'class="rdp-hero-stat-n">4x')
out_html = out_html.replace('class="rdp-hero-stat-l">And evidence', 'class="rdp-hero-stat-l">Efficiency')

with open(r'c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\about-us.html', 'w', encoding='utf-8') as f:
    f.write(out_html)
