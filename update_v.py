import os, re
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=4"', content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
