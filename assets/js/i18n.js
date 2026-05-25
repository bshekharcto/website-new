(function() {
    function initI18n() {
        try {
            console.log("i18n initialized started");
            
            // 1. Add notranslate to images
            const images = document.querySelectorAll("img");
            images.forEach(img => {
                img.classList.add("notranslate");
                if (img.parentElement) {
                    const parent = img.parentElement;
                    if (parent.tagName === 'FIGURE' || parent.classList.contains('caption') || parent.classList.contains('image-wrapper')) {
                        parent.classList.add("notranslate");
                    }
                }
            });

            // 2. Inject CSS
            const style = document.createElement('style');
            style.innerHTML = `
                .skiptranslate iframe, .VIpgJd-Zvi9od-ORHb-OEVmcd, #goog-gt-tt, .VIpgJd-Zvi9od-aZ2wEe-wOHMyf { display: none !important; }
                body { top: 0px !important; }
                .nav-wrap { padding-right: 100px !important; } /* Prevent overlap with lang switcher */
                #custom-lang-switcher {
                    position: fixed !important;
                    top: 24px !important;
                    right: 20px !important;
                    z-index: 2147483647 !important;
                    font-family: 'Inter', system-ui, sans-serif !important;
                }
                .lang-btn {
                    background: rgba(255, 255, 255, 0.95) !important;
                    backdrop-filter: blur(10px) !important;
                    border: 1px solid rgba(0,0,0,0.1) !important;
                    border-radius: 12px !important;
                    padding: 6px 12px !important;
                    font-size: 13px !important;
                    font-weight: 700 !important;
                    cursor: pointer !important;
                    display: flex !important;
                    align-items: center !important;
                    gap: 6px !important;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
                    transition: all 0.2s ease !important;
                }
                .lang-btn.lang-en {
                    color: #0056b3 !important;
                    border-color: rgba(0, 86, 179, 0.3) !important;
                }
                .lang-btn.lang-en svg {
                    stroke: #0056b3 !important;
                }
                .lang-btn.lang-fr {
                    color: #d32f2f !important;
                    border-color: rgba(211, 47, 47, 0.3) !important;
                }
                .lang-btn.lang-fr svg {
                    stroke: #d32f2f !important;
                }
                .lang-btn:hover {
                    box-shadow: 0 4px 12px rgba(0,0,0,0.12) !important;
                    transform: translateY(-1px) !important;
                }
                .lang-dropdown {
                    position: absolute !important;
                    top: 100% !important;
                    right: 0 !important;
                    margin-top: 8px !important;
                    background: #fff !important;
                    border-radius: 8px !important;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
                    border: 1px solid rgba(0,0,0,0.05) !important;
                    display: flex !important;
                    flex-direction: column !important;
                    min-width: 120px !important;
                    overflow: hidden !important;
                    opacity: 0;
                    pointer-events: none;
                    transform: translateY(-10px);
                    transition: all 0.2s ease !important;
                }
                .lang-dropdown.show {
                    opacity: 1;
                    pointer-events: auto;
                    transform: translateY(0);
                }
                .lang-option {
                    padding: 10px 16px !important;
                    font-size: 12px !important;
                    color: #555 !important;
                    cursor: pointer !important;
                    transition: background 0.2s !important;
                }
                .lang-option:hover {
                    background: #f5f7fa !important;
                    color: #000 !important;
                }
                #google_translate_element { display: none !important; }
            `;
            document.head.appendChild(style);

            function getCookie(name) {
                let match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
                if (match) return match[2];
                return null;
            }
            
            const currentLang = getCookie('googtrans');
            const isFr = currentLang && currentLang.includes('/fr');

            // 3. Inject UI
            const switcherDiv = document.createElement('div');
            switcherDiv.id = 'custom-lang-switcher';
            switcherDiv.className = 'notranslate'; 
            const activeClass = isFr ? 'lang-fr' : 'lang-en';
            switcherDiv.innerHTML = `
                <button id="lang-menu-btn" class="lang-btn ${activeClass}">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                    <span id="lang-btn-text">${isFr ? 'FR' : 'EN'}</span>
                </button>
                <div id="lang-dropdown" class="lang-dropdown">
                    <div class="lang-option" data-lang="en">English (EN)</div>
                    <div class="lang-option" data-lang="fr">Français (FR)</div>
                </div>
                <div id="google_translate_element"></div>
            `;
            
            // Append to body (outside menu bar)
            document.body.insertBefore(switcherDiv, document.body.firstChild);
            
            const menuBtn = document.getElementById('lang-menu-btn');
            const dropdown = document.getElementById('lang-dropdown');
            
            menuBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                dropdown.classList.toggle('show');
            });
            
            document.addEventListener('click', () => {
                dropdown.classList.remove('show');
            });
            
            document.querySelectorAll('.lang-option').forEach(opt => {
                opt.addEventListener('click', function() {
                    setLanguage(this.getAttribute('data-lang'));
                });
            });
            
            console.log("i18n UI appended to DOM");

            // 4. Change language logic
            function setLanguage(lang) {
                try {
                    let domain = window.location.hostname;
                    let cookieDomain = domain ? '; domain=' + domain : '';
                    if (lang === 'fr') {
                        document.cookie = 'googtrans=/en/fr; path=/' + cookieDomain;
                        document.cookie = 'googtrans=/en/fr; path=/';
                    } else {
                        document.cookie = 'googtrans=/en/en; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/' + cookieDomain;
                        document.cookie = 'googtrans=/en/en; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
                        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/' + cookieDomain;
                        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
                    }
                    window.location.reload();
                } catch(e) {
                    console.error("setLanguage error:", e);
                }
            }

            // 5. IP Check Logic
            try {
                const hasVisited = localStorage.getItem('lang_checked');
                if (!hasVisited && !currentLang) {
                    fetch('https://ipapi.co/json/')
                        .then(response => response.json())
                        .then(data => {
                            localStorage.setItem('lang_checked', 'true');
                            if (data.country_code === 'FR') {
                                setLanguage('fr');
                            }
                        })
                        .catch(error => console.warn("IP Check Failed", error));
                }
            } catch (e) {
                console.warn("LocalStorage access failed", e);
            }

            // 6. Load Google Translate API
            window.googleTranslateElementInit = function() {
                try {
                    new google.translate.TranslateElement({
                        pageLanguage: 'en',
                        includedLanguages: 'fr',
                        autoDisplay: false
                    }, 'google_translate_element');
                } catch(e) { console.error("Translate init failed", e); }
            };

            const gtScript = document.createElement('script');
            gtScript.type = 'text/javascript';
            gtScript.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
            document.body.appendChild(gtScript);

        } catch (globalErr) {
            console.error("i18n global error:", globalErr);
        }
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initI18n);
    } else {
        initI18n();
    }
})();
