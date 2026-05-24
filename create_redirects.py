import os

redirects = {
    "about-us": "/",
    "industry/mining": "/pages/solutions/mining.html",
    "usecase/efficient-fleet-management": "/pages/platform/cortex.html",
    "contact-us": "/#b2b-demo-form",
    "industry/logistics-industry": "/pages/platform/cortex.html",
    "industry/highway-construction": "/pages/solutions/highway.html"
}

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={url}">
    <link rel="canonical" href="https://www.cognecto.com{url}">
    <title>Redirecting...</title>
    <script>
        window.location.replace("{url}");
    </script>
</head>
<body>
    <p>If you are not redirected automatically, <a href="{url}">click here</a>.</p>
</body>
</html>
"""

base_dir = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"

for path, target in redirects.items():
    dir_path = os.path.join(base_dir, os.path.normpath(path))
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_template.format(url=target))
    
    print(f"Created redirect for {path} -> {target}")
