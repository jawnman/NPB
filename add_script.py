import os

base = r"C:\Users\nickr\.gemini\antigravity\brain\e4e1be1e-4d82-467f-affd-f24bdf5991eb\barbershop"

for page in ["contact.html", "gallery.html"]:
    path = os.path.join(base, page)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    
    if '<script src="js/script.js"></script>' not in html:
        html = html.replace('</body>', '    <script src="js/script.js"></script>\n</body>')
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Added script to {page}")
    else:
        print(f"Script already in {page}")
