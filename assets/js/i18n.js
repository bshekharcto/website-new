document.addEventListener("DOMContentLoaded", function() {
    // 1. Add notranslate to images and their immediate parent elements to preserve English
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

    // 2. Inject CSS for Switcher UI & Google Translate tweaks
    const style = document.createElement('style');
    style.innerHTML = `
        /* Hide Google Translate Toolbar completely */
        .skiptranslate iframe,
        .VIpgJd-Zvi9od-ORHb-OEVmcd,
        #goog-gt-tt,
        .VIpgJd-Zvi9od-aZ2wEe-wOHMyf {
            display: none !important;
        }
        body {
            top: 0px !important;
        }
        /* Custom Switcher UI */
        .lang-switcher-container {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 999999;
            background: #ffffff;
            border-radius: 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            padding: 5px;
            border: 1px solid #eaeaea;
            font-family: 'Inter', system-ui, sans-serif;
            transition: box-shadow 0.3s ease;
        }
        .lang-switcher-container:hover {
            box-shadow: 0 6px 14px rgba(0,0,0,0.15);
        }
        .lang-btn {
            background: none;
            border: none;
            padding: 6px 16px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            border-radius: 20px;
            color: #666;
            transition: all 0.2s ease;
            outline: none;
        }
        .lang-btn:hover:not(.active) {
            background: #f0f0f0;
            color: #333;
        }
        .lang-btn.active {
            background: #0056b3;
            color: #ffffff;
            box-shadow: 0 2px 4px rgba(0,86,179,0.3);
        }
        /* Hidden GT Element */
        #google_translate_element {
            display: none;
        }
    `;
    document.head.appendChild(style);

    // 3. Inject Switcher UI HTML
    const switcherDiv = document.createElement('div');
    switcherDiv.className = 'lang-switcher-container notranslate'; 
    switcherDiv.innerHTML = `
        <button class="lang-btn" id="btn-en">EN</button>
        <button class="lang-btn" id="btn-fr">FR</button>
        <div id="google_translate_element"></div>
    `;
    document.body.appendChild(switcherDiv);

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

    // 4. IP Check Logic
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
            .catch(error => console.error("IP Check Failed", error));
    }

    // 5. Change language
    function setLanguage(lang) {
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
    }

    document.getElementById('btn-en').addEventListener('click', () => {
        if (!document.getElementById('btn-en').classList.contains('active')) {
            setLanguage('en');
        }
    });

    document.getElementById('btn-fr').addEventListener('click', () => {
        if (!document.getElementById('btn-fr').classList.contains('active')) {
            setLanguage('fr');
        }
    });

    // 6. Load Google Translate API
    window.googleTranslateElementInit = function() {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'fr',
            autoDisplay: false
        }, 'google_translate_element');
    };

    const gtScript = document.createElement('script');
    gtScript.type = 'text/javascript';
    gtScript.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    document.body.appendChild(gtScript);
});
