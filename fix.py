import re

with open('services-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Unveil Card Image panels to be full bleed
content = re.sub(
    r'class="unveil-card-right" style="width: 50%; background: #222; display: flex; align-items: center; justify-content: center; position: relative; padding: 24px;">\s*<img src="([^"]+)" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px; box-shadow: 0 16px 40px rgba\(0,0,0,0\.1\);" class="unveil-img">',
    r'class="unveil-card-right" style="width: 50%; background: #222; display: flex; align-items: center; justify-content: center; position: relative; padding: 0;">\n                                            <img src="\1" style="width: 100%; height: 100%; object-fit: cover; border-radius: 0; box-shadow: none;" class="unveil-img">',
    content, flags=re.DOTALL
)

with open('services-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated unveil cards!")
