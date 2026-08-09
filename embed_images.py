import base64
import re
from PIL import Image
import io

def process_image(img_path, max_size):
    with Image.open(img_path) as img:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG", optimize=True)
        return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode('utf-8')

print("Processing character.png...")
char_b64 = process_image("character.png", (400, 500))

print("Processing photo.png...")
photo_b64 = process_image("photo.png", (200, 200))

def replace_in_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updating hero.svg...")
replace_in_file("hero.svg", r'href="\./character\.png"', f'href="{char_b64}"')

print("Updating hero-light.svg...")
replace_in_file("hero-light.svg", r'href="\./character\.png"', f'href="{char_b64}"')

print("Updating lanyard.svg...")
replace_in_file("lanyard.svg", r'href="\./photo\.png"', f'href="{photo_b64}"')

print("Done!")
