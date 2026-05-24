import os
import re

filepath = r"c:\Users\bhanu\.gemini\antigravity-ide\scratch\website-new\pages\resources\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the 4 cards
sources_to_remove = ["ZaubaCorp", "Google Play", "Tofler", "Startup India"]

# Each card starts with <a href="..." target="_blank" rel="noopener noreferrer" class="res-card news-card"
# and ends with </a>
# We can use regex to find all cards and only keep the ones that don't match the sources

def filter_cards(match):
    card_html = match.group(0)
    for source in sources_to_remove:
        if f">{source}</div>" in card_html or f">{source}</div>" in card_html:
            return ""  # Remove this card
    return card_html

# The cards are generated with this exact signature
card_pattern = re.compile(r'<a href="[^"]+" target="_blank" rel="noopener noreferrer" class="res-card news-card"[^>]*>.*?</a>', re.DOTALL)
content = card_pattern.sub(filter_cards, content)

# 2. Fix YourStory image
# It was pointing to "../../assets/images/highway_sunset_road.webp" which doesn't exist.
content = content.replace("../../assets/images/highway_sunset_road.webp", "../../assets/images/highway_nrida_thumb.webp")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed the requested cards and fixed the YourStory image.")
