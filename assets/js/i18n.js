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
                    top: 20px !important;
                    right: 20px !important;
                    z-index: 2147483647 !important; /* Max z-index */
                    background: #ffffff !important;
                    border-radius: 30px !important;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
                    display: flex !important;
                    align-items: center !important;
                    padding: 5px !important;
                    border: 2px solid #0056b3 !important;
                    font-family: Arial, sans-serif !important;
                }
                .lang-btn {
                    background: none !important;
                    border: none !important;
                    padding: 8px 16px !important;
                    font-size: 14px !important;
                    font-weight: bold !important;
                    cursor: pointer !important;
                    border-radius: 20px !important;
                    color: #333 !important;
                    outline: none !important;
                }
                .lang-btn.active {
                    background: #0056b3 !important;
                    color: #ffffff !important;
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
            // Try to prepend to body to ensure it's not hidden under a sticky footer or something
            document.body.insertBefore(switcherDiv, document.body.firstChild);
            console.log("i18n UI appended to body");

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
                    let cookieDomain = domain ? \`; domain=\${domain}\` : '';
                    if (lang === 'fr') {
                        document.cookie = \`googtrans=/en/fr; path=/\${cookieDomain}\`;
                        document.cookie = \`googtrans=/en/fr; path=/\`;
                    } else {
                        document.cookie = \`googtrans=/en/en; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/\${cookieDomain}\`;
                        document.cookie = \`googtrans=/en/en; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/\`;
                        document.cookie = \`googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/\${cookieDomain}\`;
                        document.cookie = \`googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/\`;
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
