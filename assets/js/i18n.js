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
                #custom-lang-switcher {
                    position: fixed !important;
                    top: 24px !important; /* Adjusted to vertically center with the menu bar */
                    right: 20px !important;
                    z-index: 2147483647 !important;
                    background: rgba(255, 255, 255, 0.7) !important;
                    backdrop-filter: blur(10px) !important;
                    border-radius: 12px !important;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
                    display: flex !important;
                    align-items: center !important;
                    padding: 3px !important;
                    border: 1px solid rgba(0,0,0,0.05) !important;
                    font-family: 'Inter', system-ui, sans-serif !important;
                }
                .lang-btn {
                    background: transparent !important;
                    border: none !important;
                    padding: 4px 8px !important;
                    font-size: 11px !important;
                    font-weight: 600 !important;
                    cursor: pointer !important;
                    border-radius: 8px !important;
                    color: #888 !important;
                    outline: none !important;
                    transition: all 0.2s ease !important;
                    letter-spacing: 0.5px !important;
                }
                .lang-btn:hover {
                    color: #333 !important;
                }
                .lang-btn.active {
                    background: #ffffff !important;
                    color: #111 !important;
                    box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
                }
                #google_translate_element { display: none !important; }
            `;
            document.head.appendChild(style);

            // 3. Inject UI
            const switcherDiv = document.createElement('div');
            switcherDiv.id = 'custom-lang-switcher';
            switcherDiv.className = 'notranslate'; 
            switcherDiv.innerHTML = `
                <button class="lang-btn" id="btn-en">EN</button>
                <button class="lang-btn" id="btn-fr">FR</button>
                <div id="google_translate_element"></div>
            `;
            
            // Append to body (outside menu bar)
            document.body.insertBefore(switcherDiv, document.body.firstChild);
            console.log("i18n UI appended to DOM");

            function getCookie(name) {
                let match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
                if (match) return match[2];
                return null;
            }

            const currentLang = getCookie('googtrans');
            if (currentLang && currentLang.includes('/fr')) {
                document.getElementById('btn-fr').classList.add('active');
            } else {
                document.getElementById('btn-en').classList.add('active');
            }

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

            document.getElementById('btn-en').addEventListener('click', () => {
                if (!document.getElementById('btn-en').classList.contains('active')) setLanguage('en');
            });

            document.getElementById('btn-fr').addEventListener('click', () => {
                if (!document.getElementById('btn-fr').classList.contains('active')) setLanguage('fr');
            });

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
