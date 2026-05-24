import os
import json

filepath = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject the Tab Switcher
tabs_html = """
    <div class="res-main-tabs" style="display:flex; gap:1.5rem; margin-bottom:2rem; border-bottom:1px solid var(--rule);">
      <button class="res-main-tab active" data-target="documents" style="padding:0.75rem 0.5rem; font-family:var(--display); font-size:16px; font-weight:700; color:var(--blue); border-bottom:3px solid var(--blue); transition:all 0.2s;">Documents</button>
      <button class="res-main-tab" data-target="news" style="padding:0.75rem 0.5rem; font-family:var(--display); font-size:16px; font-weight:500; color:var(--ink-3); border-bottom:3px solid transparent; transition:all 0.2s;">News & Recognition</button>
    </div>
"""

content = content.replace('<div class="res-filter-stack">', tabs_html + '      <div class="res-filter-stack" id="documents-filters">')

# 2. Add News Filters (hidden by default)
news_filters_html = """
      <div class="res-filter-stack" id="news-filters" style="display:none;">
        <div class="res-filter-row" style="flex-wrap:wrap; gap:0.5rem;">
          <span class="res-filter-label" style="margin-right:1rem; padding-top:0.3rem;">Category</span>
          <button class="res-filter-pill active" data-news-filter="all">All</button>
          <button class="res-filter-pill" data-news-filter="news">News</button>
          <button class="res-filter-pill" data-news-filter="government-recognition">Government Recognition</button>
          <button class="res-filter-pill" data-news-filter="funding">Funding</button>
          <button class="res-filter-pill" data-news-filter="accelerator">Accelerator</button>
          <button class="res-filter-pill" data-news-filter="customer-deployment">Customer Deployment</button>
          <button class="res-filter-pill" data-news-filter="product-app-store">Product / App Store</button>
          <button class="res-filter-pill" data-news-filter="company-verification">Company Verification</button>
        </div>
      </div>
"""
content = content.replace('</div>\n    </div>\n  </div>\n</section>', '</div>\n    </div>\n' + news_filters_html + '  </div>\n</section>')

# 3. Add News Grid (hidden by default)
news_items = [
    {
        "priority": 1,
        "title": "Cognecto featured by YourStory for mining and logistics innovation",
        "desc": "YourStory profiles Cognecto’s IoT and sensor-driven platform for improving mining, logistics, transportation, and heavy equipment operations.",
        "type": "News",
        "url": "https://yourstory.com/2025/01/cognecto-makes-mining-logistics-work-easy-iot-sensor-solutions",
        "img": "../../assets/images/highway_infra_future.webp",
        "source": "YourStory",
        "filter": "news"
    },
    {
        "priority": 2,
        "title": "Cognecto selected in YourStory Tech30 2024",
        "desc": "Cognecto was listed among YourStory’s Tech30 promising Indian startups for 2024, recognised as a connected operations cloud.",
        "type": "News",
        "url": "https://yourstory.com/2024/09/tech30-thirty-most-promising-indian-startups-of-2024",
        "img": "../../assets/images/highway_sunset_road.webp",
        "source": "YourStory",
        "filter": "news"
    },
    {
        "priority": 3,
        "title": "Cognecto selected for IndiaAI Global Acceleration Programme",
        "desc": "PIB / MeitY listed Cognecto among 10 Indian AI startups selected for the IndiaAI Startups Global Acceleration Programme.",
        "type": "Government Recognition",
        "url": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2252858",
        "img": "https://images.pexels.com/photos/1078884/pexels-photo-1078884.jpeg?auto=compress&cs=tinysrgb&w=900&h=600&fit=crop",
        "source": "PIB / MeitY",
        "filter": "government-recognition"
    },
    {
        "priority": 4,
        "title": "Cognecto listed in Startup India IMB approved cases",
        "desc": "Startup India’s official IMB approved cases PDF lists Cognecto Private Limited with certificate number DIPP72270.",
        "type": "Government Recognition",
        "url": "https://www.startupindia.gov.in/content/dam/invest-india/Templates/public/IMB/imb_meetings/eighty-two-meeting-of-imb.pdf",
        "img": "../../assets/images/mining_excavator_dumper.webp",
        "source": "Startup India",
        "filter": "government-recognition"
    },
    {
        "priority": 5,
        "title": "Cognecto raises ₹4 crore seed round led by Inflection Point Ventures",
        "desc": "Entrackr reported Cognecto’s seed funding round led by Inflection Point Ventures to strengthen AI-based solutions.",
        "type": "Funding",
        "url": "https://entrackr.com/2023/04/ipv-leads-rs-4-cr-round-in-cognecto/",
        "img": "https://images.pexels.com/photos/2219024/pexels-photo-2219024.jpeg?auto=compress&cs=tinysrgb&w=900&h=600&fit=crop",
        "source": "Entrackr",
        "filter": "funding"
    },
    {
        "priority": 6,
        "title": "VCCircle reports IPV investment in Cognecto",
        "desc": "VCCircle covered Cognecto’s seed funding and its AI, predictive analytics, and managed services focus for heavy industries.",
        "type": "Funding",
        "url": "https://www.vccircle.com/inflectionpoint-ventures-writes-seed-cheque-to-iot-solutions-provider-cognecto",
        "img": "../../assets/images/highway_construction_asphalt.webp",
        "source": "VCCircle",
        "filter": "funding"
    },
    {
        "priority": 7,
        "title": "RKS Construction chooses Cognecto for enterprise-wide heavy equipment management",
        "desc": "PRNewswire reported RKS Construction’s enterprise-wide implementation of Cognecto’s Heavy Equipment Management Platform.",
        "type": "Customer Deployment",
        "url": "https://www.prnewswire.com/news-releases/ram-kripal-singh-rks-construction-indias-leading-construction-company-chooses-cognecto-heavy-equipment-management-platform-for-enterprise-wide-implementation-301551151.html",
        "img": "../../assets/images/mining_dump_truck.webp",
        "source": "PRNewswire",
        "filter": "customer-deployment"
    },
    {
        "priority": 8,
        "title": "Cognecto featured for Western Australia mining expansion",
        "desc": "Spacecubed / Perth Landing Pad featured Cognecto’s vision for transforming mining operations in Western Australia.",
        "type": "Accelerator",
        "url": "https://blog.spacecubed.com/cognectos-vision-for-transforming-mining-operations-in-western-australia-with-the-support-of-perth-landing-pad/",
        "img": "../../assets/images/mining_aerial_quarry.webp",
        "source": "Spacecubed",
        "filter": "accelerator"
    },
    {
        "priority": 9,
        "title": "Cognecto selected for Qatar TASMU Accelerator 2024",
        "desc": "Business Startup Qatar reported Cognecto among the startups selected for TASMU Accelerator 2024.",
        "type": "Accelerator",
        "url": "https://www.businessstartupqatar.com/news/qatar-tasmu-accelerator-announces-25-startups/",
        "img": "https://images.pexels.com/photos/1004409/pexels-photo-1004409.jpeg?auto=compress&cs=tinysrgb&w=900&h=600&fit=crop",
        "source": "Startup Qatar",
        "filter": "accelerator"
    },
    {
        "priority": 10,
        "title": "CIO Insider profile on Cognecto’s heavy equipment platform",
        "desc": "CIO Insider describes Cognecto’s heavy equipment monitoring and optimisation platform for owned and rented assets.",
        "type": "News",
        "url": "https://www.cioinsiderindia.com/vendor/cognecto-leveraging-ai-to-offer-an-advanced-fleet-management-platform-cid-1406.html",
        "img": "../../assets/images/highway_bro_main.webp",
        "source": "CIO Insider",
        "filter": "news"
    },
    {
        "priority": 11,
        "title": "Cognecto app listed on Google Play",
        "desc": "Google Play lists the Cognecto app and describes the platform as edge-to-analytics software for real-time equipment status.",
        "type": "Product / App Store",
        "url": "https://play.google.com/store/apps/details?id=com.app.cognecto&hl=en",
        "img": "../../assets/images/highway_rural_construction.webp",
        "source": "Google Play",
        "filter": "product-app-store"
    },
    {
        "priority": 12,
        "title": "Cognecto edge device launch syndicated on EIN Presswire",
        "desc": "EIN Presswire carried Cognecto’s product launch for an AI edge device for mining, construction, material handling, and logistics.",
        "type": "News",
        "url": "https://www.einpresswire.com/article/551768201/cognecto-launches-new-product-enabling-ai-for-heavy-equipments-in-mining-construction-and-logistics",
        "img": "../../assets/images/mining_worker_bulldozer.webp",
        "source": "EIN Presswire",
        "filter": "news"
    },
    {
        "priority": 13,
        "title": "ETEnergyWorld covers Cognecto seed funding",
        "desc": "Economic Times EnergyWorld reported Cognecto’s ₹4 crore seed funding led by Inflection Point Ventures.",
        "type": "Funding",
        "url": "https://energy.economictimes.indiatimes.com/news/coal/ai-solution-company-cognecto-raises-rs-4-cr-in-seed-round-led-by-inflection-point-ventures/99644426",
        "img": "https://images.pexels.com/photos/1267338/pexels-photo-1267338.jpeg?auto=compress&cs=tinysrgb&w=900&h=600&fit=crop",
        "source": "ETEnergyWorld",
        "filter": "funding"
    },
    {
        "priority": 14,
        "title": "Entrepreneur India covers Cognecto funding",
        "desc": "Entrepreneur India covered Cognecto’s seed funding and its AI-led operational analytics for mining and construction.",
        "type": "Funding",
        "url": "https://india.entrepreneur.com/news-and-trends/ai-solution-company-cognecto-raises-inr-4-crore-in-seed/450030",
        "img": "https://images.pexels.com/photos/416405/pexels-photo-416405.jpeg?auto=compress&cs=tinysrgb&w=900&h=600&fit=crop",
        "source": "Entrepreneur India",
        "filter": "funding"
    },
    {
        "priority": 15,
        "title": "Tofler company profile for Cognecto",
        "desc": "Tofler provides third-party company registration and corporate profile details for Cognecto Private Limited.",
        "type": "Company Verification",
        "url": "https://www.tofler.in/cognecto-private-limited/company/U72900KA2019PTC125311",
        "img": "../../assets/images/highway_during_construction_compaction.webp",
        "source": "Tofler",
        "filter": "company-verification"
    },
    {
        "priority": 16,
        "title": "ZaubaCorp company profile for Cognecto",
        "desc": "ZaubaCorp lists corporate registration information, CIN, incorporation details, and registered office data for Cognecto Private Limited.",
        "type": "Company Verification",
        "url": "https://www.zaubacorp.com/COGNECTO-PRIVATE-LIMITED-U72900KA2019PTC125311",
        "img": "../../assets/images/highway_construction_road_base.webp",
        "source": "ZaubaCorp",
        "filter": "company-verification"
    }
]

news_grid_html = '<div class="res-grid" id="news-grid" style="display:none;">\n'
for item in news_items:
    news_grid_html += f"""        <a href="{item['url']}" target="_blank" rel="noopener noreferrer" class="res-card news-card" data-news-category="{item['filter']}">
          <div class="res-card-img">
            <img src="{item['img']}" alt="{item['title']}" loading="lazy"/>
            <div class="res-card-img-overlay" style="background:linear-gradient(160deg,rgba(14,27,53,0.3) 0%,#1A2540 100%); opacity:0.6;"></div>
            <div style="position:absolute; top:1rem; left:1rem; z-index:2; background:rgba(255,255,255,0.9); backdrop-filter:blur(10px); border-radius:6px; padding:6px 12px; font-family:var(--display); font-size:12px; font-weight:800; color:var(--ink); box-shadow:0 4px 12px rgba(0,0,0,0.15);">{item['source']}</div>
          </div>
          <div class="res-card-body">
            <div class="res-card-meta">
              <span class="res-card-sector" style="color:var(--blue); font-weight:700;">{item['type']}</span>
              <span class="res-card-dot">·</span>
              <span class="res-card-time">External Link</span>
            </div>
            <div class="res-card-title" style="font-size:1.15rem; line-height:1.4;">{item['title']}</div>
            <div class="res-card-blurb" style="font-size:13px;">{item['desc']}</div>
            <div class="res-card-footer" style="margin-top:auto; padding-top:1rem;">
              <span class="res-card-cta" style="color:var(--blue);">Read More ↗</span>
            </div>
          </div>
        </a>\n"""
news_grid_html += '      </div>\n'

content = content.replace('<div class="res-grid" id="res-grid">', '<div id="documents-wrap">\n    <div class="res-grid" id="res-grid">')
content = content.replace('<div class="res-empty" id="res-empty">No resources match this filter — try another combination.</div>\n  </div>\n</section>', '<div class="res-empty" id="res-empty">No resources match this filter — try another combination.</div>\n    </div><!-- /documents-wrap -->\n    <div id="news-wrap" style="display:none;">\n      ' + news_grid_html + '      <div class="res-empty" id="news-empty" style="display:none;">No news items match this filter.</div>\n    </div><!-- /news-wrap -->\n  </div>\n</section>')

# 4. Add Tab and News Filter Javascript
js_script = """

// Tab Switching Logic
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.res-main-tab');
  const docFilters = document.getElementById('documents-filters');
  const newsFilters = document.getElementById('news-filters');
  const docWrap = document.getElementById('documents-wrap');
  const newsWrap = document.getElementById('news-wrap');

  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      // Update active tab
      tabs.forEach(t => {
        t.classList.remove('active');
        t.style.fontWeight = '500';
        t.style.color = 'var(--ink-3)';
        t.style.borderBottomColor = 'transparent';
      });
      this.classList.add('active');
      this.style.fontWeight = '700';
      this.style.color = 'var(--blue)';
      this.style.borderBottomColor = 'var(--blue)';

      // Show/Hide sections
      if (this.getAttribute('data-target') === 'documents') {
        docFilters.style.display = 'block';
        docWrap.style.display = 'block';
        newsFilters.style.display = 'none';
        newsWrap.style.display = 'none';
      } else {
        docFilters.style.display = 'none';
        docWrap.style.display = 'none';
        newsFilters.style.display = 'block';
        newsWrap.style.display = 'block';
        // Make sure grid is shown (might be hidden by my inline style)
        document.getElementById('news-grid').style.display = 'grid';
      }
    });
  });

  // News Filtering Logic
  const newsFilterBtns = document.querySelectorAll('#news-filters .res-filter-pill');
  const newsCards = document.querySelectorAll('.news-card');
  const newsEmpty = document.getElementById('news-empty');

  newsFilterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      newsFilterBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      
      const filter = this.getAttribute('data-news-filter');
      let count = 0;
      
      newsCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-news-category') === filter) {
          card.style.display = 'flex';
          setTimeout(() => card.style.opacity = '1', 50);
          count++;
        } else {
          card.style.opacity = '0';
          setTimeout(() => card.style.display = 'none', 150);
        }
      });
      
      setTimeout(() => {
        if (count === 0) {
          newsEmpty.style.display = 'block';
        } else {
          newsEmpty.style.display = 'none';
        }
      }, 160);
    });
  });
  
  // Check hash on load to open News tab if needed
  if (window.location.hash === '#news') {
    document.querySelector('.res-main-tab[data-target="news"]').click();
  }
});
"""
content = content.replace('// Filter logic — supports BOTH type + se', js_script + '\n\n// Filter logic — supports BOTH type + se')

# 5. Fix mega menu links
content = content.replace('<!-- Blog & Insights -->\n                  <a href="index.html" class="mega-aud-card">', '<!-- Blog & Insights -->\n                  <a href="index.html#news" class="mega-aud-card">')
content = content.replace('<div class="mega-aud-title">Blog &amp; Insights</div>', '<div class="mega-aud-title">News &amp; Insights</div>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html successfully.")
