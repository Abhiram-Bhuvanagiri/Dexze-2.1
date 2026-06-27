import re

with open('services-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update storytelling-pin-container background to white (if it was #161616)
content = content.replace(
    'justify-content: center; background-color: #161616;">\n                        <div class="container" style="max-width: 1400px; width: 100%; margin: 0 auto; padding: 0 32px; display: flex; align-items: center; justify-content: space-between; gap: 64px; height: 60vh; position: relative;">',
    'justify-content: center; background-color: #ffffff;">\n                        <div class="container" style="max-width: 1400px; width: 100%; margin: 0 auto; padding: 0; display: flex; align-items: stretch; justify-content: center; height: 60vh; position: relative; border-radius: 24px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.08); background: #1a1a1a;">'
)

# Also handle case if it was #ffffff already
content = content.replace(
    'justify-content: center; background-color: #ffffff;">\n                        <div class="container" style="max-width: 1400px; width: 100%; margin: 0 auto; padding: 0 32px; display: flex; align-items: center; justify-content: space-between; gap: 64px; height: 60vh; position: relative;">',
    'justify-content: center; background-color: #ffffff;">\n                        <div class="container" style="max-width: 1400px; width: 100%; margin: 0 auto; padding: 0; display: flex; align-items: stretch; justify-content: center; height: 60vh; position: relative; border-radius: 24px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.08); background: #1a1a1a;">'
)


# 2. Update story-image-panel to be 50% and full bleed
content = content.replace(
    '<div class="story-image-panel" style="width: 45%; height: 100%; position: relative; overflow: hidden; border-radius: 16px; box-shadow: 0 20px 48px rgba(0,0,0,0.06); background: #f4f6f8;">',
    '<div class="story-image-panel" style="width: 50%; height: 100%; position: relative; overflow: hidden; border-radius: 0; box-shadow: none; background: #222;">'
)

# 3. Update story-text-panel to be 50% and have appropriate padding
content = content.replace(
    '<div class="story-text-panel" style="width: 45%; height: 100%; position: relative; display: flex; align-items: center; padding-left: 32px;">',
    '<div class="story-text-panel" style="width: 50%; height: 100%; position: relative; display: flex; align-items: center; padding: 40px 4vw;">'
)

with open('services-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated Idea to Life layout!")
