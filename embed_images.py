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

print("Processing profile-hero.png...")
char_b64 = process_image("assets/profile-hero.png", (400, 500))

print("Processing profile-avatar.png...")
photo_b64 = process_image("assets/profile-avatar.png", (300, 300))

def replace_in_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(pattern, replacement, content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updating hero.svg...")
replace_in_file("hero.svg", r'href="\./assets/profile-hero\.png"', f'href="{char_b64}"')

print("Updating lanyard.svg...")
replace_in_file("lanyard.svg", r'href="\./assets/profile-avatar\.png"', f'href="{photo_b64}"')

print("Done!")
