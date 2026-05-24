import os

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
pages = [
    "pages/solutions/highway.html",
    "pages/solutions/mining.html",
    "pages/solutions/water.html",
    "pages/solutions/ehs.html",
    "pages/platform/boson.html",
    "pages/platform/photon.html",
    "pages/platform/cortex.html"
]

old_js = """<script>
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
</script>"""

new_js = """<script>
  (function(){
    function initFAQ() {
      const faqItems = document.querySelectorAll('.faq-item');
      faqItems.forEach(item => {
        const btn = item.querySelector('.faq-question');
        if (btn) {
          // Remove old listeners by cloning
          const newBtn = btn.cloneNode(true);
          btn.parentNode.replaceChild(newBtn, btn);
          newBtn.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            // Only toggle items that have .faq-question to avoid old FAQ collisions
            faqItems.forEach(i => {
                if(i.querySelector('.faq-question')) i.classList.remove('active');
            });
            if (!isActive) item.classList.add('active');
          });
        }
      });
    }
    
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initFAQ);
    } else {
      initFAQ();
    }
  })();
</script>"""

for p in pages:
    filepath = os.path.join(BASE_DIR, p)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if old_js in html:
            html = html.replace(old_js, new_js)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Fixed {filepath}")
        else:
            print(f"Old JS not found in {filepath}")
