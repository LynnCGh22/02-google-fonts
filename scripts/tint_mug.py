from PIL import Image, ImageOps

src = 'img/mug.png'
dst = 'img/mug-lightgray.png'

img = Image.open(src).convert('RGBA')
# Separate alpha
alpha = img.split()[-1]
# Convert to grayscale RGB
gray = ImageOps.grayscale(img.convert('RGB')).convert('RGB')
# Create a light-gray image
light_gray = Image.new('RGB', img.size, (220,220,220))
# Blend gray with light_gray to keep details but shift tone
tinted_rgb = Image.blend(gray, light_gray, alpha=0.6)
# Combine with original alpha
tinted_rgba = tinted_rgb.convert('RGBA')
tinted_rgba.putalpha(alpha)
# Save result
tinted_rgba.save(dst)
print(f"Saved {dst}")
