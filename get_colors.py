from PIL import Image

def get_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

img = Image.open('img/logo.png').convert('RGB')
pixels = list(img.getdata())

# Find brightest red/blue
max_r = max_b = (0,0,0)
for p in pixels:
    if p[0] > max_r[0] and p[0] > p[1] + 50 and p[0] > p[2] + 50:
        max_r = p
    if p[2] > max_b[2] and p[2] > p[0] + 50 and p[2] > p[1] + 50:
        max_b = p

print(f"Neon Red: {get_hex(max_r)}")
print(f"Neon Blue: {get_hex(max_b)}")
