from PIL import Image

path = r"C:\Users\nickr\.gemini\antigravity\brain\e4e1be1e-4d82-467f-affd-f24bdf5991eb\barbershop\favicon.png"
img = Image.open(path)
w, h = img.size

# Make it a square by creating a new transparent/white background and pasting it in the middle, or by cropping.
# If it's a logo, it's probably best to pad it to a square so we don't cut off any text.
size = max(w, h)
new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0)) # transparent padding
new_img.paste(img, ((size - w) // 2, (size - h) // 2))

# Save
new_img.save(path)
print("Padded favicon to square.")
