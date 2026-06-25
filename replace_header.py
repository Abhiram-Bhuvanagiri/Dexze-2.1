import glob
import re
import os

# Read the header from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'<header>.*?</header>', index_content, flags=re.DOTALL)
if not header_match:
    print("Could not find <header> tag in index.html")
    exit(1)

new_header = header_match.group(0)

# Replace in all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    if file == 'index.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<header>' in content and '</header>' in content:
        new_content = re.sub(r'<header>.*?</header>', new_header.replace('\\', '\\\\'), content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated header in {file}")

print("Done")
