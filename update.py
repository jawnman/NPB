import os

base = r"C:\Users\nickr\.gemini\antigravity\brain\e4e1be1e-4d82-467f-affd-f24bdf5991eb\barbershop"

old_nav_home = """            <nav class="main-nav">
                <a href="#hero">Home</a>
                <a href="#barbers">Our Barbers</a>
                <a href="gallery.html">Gallery</a>
            </nav>"""

new_nav_home = """            <nav class="main-nav">
                <a href="#hero">Home</a>
                <a href="#barbers">Our Barbers</a>
                <a href="gallery.html">Gallery</a>
                <a href="contact.html">Contact</a>
            </nav>"""

# Update index.html
path = os.path.join(base, "index.html")
with open(path, "r", encoding="utf-8") as f:
    html = f.read()
if old_nav_home in html:
    html = html.replace(old_nav_home, new_nav_home)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

old_nav_gallery = """            <nav class="main-nav">
                <a href="index.html">Home</a>
                <a href="index.html#barbers">Our Barbers</a>
                <a href="gallery.html" class="nav-active">Gallery</a>
            </nav>"""

new_nav_gallery = """            <nav class="main-nav">
                <a href="index.html">Home</a>
                <a href="index.html#barbers">Our Barbers</a>
                <a href="gallery.html" class="nav-active">Gallery</a>
                <a href="contact.html">Contact</a>
            </nav>"""

# Update gallery.html
path = os.path.join(base, "gallery.html")
with open(path, "r", encoding="utf-8") as f:
    html = f.read()
if old_nav_gallery in html:
    html = html.replace(old_nav_gallery, new_nav_gallery)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
        
