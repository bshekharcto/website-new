(function() {
    // Clean up leftover Google Translate cookies to ensure users return to English
    try {
        let domain = window.location.hostname;
        const paths = ['/', window.location.pathname];
        const lastSlashIndex = window.location.pathname.lastIndexOf('/');
        if (lastSlashIndex > 0) {
            paths.push(window.location.pathname.substring(0, lastSlashIndex));
        }
        
        const domains = ['', domain, '.' + domain];
        let parts = domain.split('.');
        while (parts.length > 1) {
            let parentDomain = parts.join('.');
            domains.push(parentDomain);
            domains.push('.' + parentDomain);
            parts.shift();
        }
        
        paths.forEach(path => {
            if (!path) return;
            domains.forEach(dom => {
                let domStr = dom ? '; domain=' + dom : '';
                document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=' + path + domStr;
                document.cookie = 'googtrans=/en/en; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=' + path + domStr;
            });
        });
        
        localStorage.removeItem('lang_checked');
    } catch(e) {
        console.warn("Clean cookies failed", e);
    }
})();
