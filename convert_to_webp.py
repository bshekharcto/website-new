import os
import glob
from PIL import Image

BASE_DIR = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new"
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "images")

# 1. Convert Images
converted_files = {}  # old_filename -> new_filename

img_files = glob.glob(os.path.join(ASSETS_DIR, "*.*"))
for img_path in img_files:
    ext = os.path.splitext(img_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        try:
            with Image.open(img_path) as im:
                # Convert to RGB if saving as WebP from PNG with transparency, or just let Pillow handle it
                # WebP supports RGBA
                new_path = os.path.splitext(img_path)[0] + ".webp"
                im.save(new_path, "webp", quality=85)
            
            old_name = os.path.basename(img_path)
            new_name = os.path.basename(new_path)
            converted_files[old_name] = new_name
            
            # Remove old file
            os.remove(img_path)
            print(f"Converted {old_name} to {new_name}")
        except Exception as e:
            print(f"Failed to convert {img_path}: {e}")

# 2. Update references in HTML and CSS
text_files = glob.glob(os.path.join(BASE_DIR, "**/*.html"), recursive=True) + \
             glob.glob(os.path.join(BASE_DIR, "**/*.css"), recursive=True)

updated_count = 0
for filepath in text_files:
    if "raw_html" in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for old_name, new_name in converted_files.items():
        # Replace occurrences. Since we only want to replace references to our local files, 
        # and the filenames are fairly unique (e.g., highway_bro_main.jpg) we can just string replace.
        content = content.replace(old_name, new_name)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated references in {os.path.relpath(filepath, BASE_DIR)}")
        updated_count += 1

print(f"Completed! Converted {len(converted_files)} images and updated {updated_count} files.")
