import os, re
for file in [f for f in os.listdir('.') if f.endswith('.html')]:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=5"', content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
