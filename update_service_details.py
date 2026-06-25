import re

def update_file():
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()

    header_match = re.search(r'<header>.*?</header>', index_content, flags=re.DOTALL)
    footer_match = re.search(r'<footer>.*?</footer>', index_content, flags=re.DOTALL)

    if not header_match or not footer_match:
        print("Could not find <header> or <footer> tag in index.html")
        return

    new_header = header_match.group(0)
    new_footer = footer_match.group(0)

    target_file = 'service-details.html'
    
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header
    content = re.sub(r'<header>.*?</header>', lambda match: new_header, content, flags=re.DOTALL)
    # Replace footer
    content = re.sub(r'<footer>.*?</footer>', lambda match: new_footer, content, flags=re.DOTALL)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated header and footer in {target_file}")

if __name__ == '__main__':
    update_file()
