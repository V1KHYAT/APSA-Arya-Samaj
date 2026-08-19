import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

replacements = {
    'src="swami_dayanand_1786472309965.jpg"': 'src="images/swami_dayanand.jpg"',
    'src="hero_havan_1786471497788.jpg"': 'src="images/hero_havan.jpg"',
    'src="mahasammelan_1786472019430.jpg"': 'src="images/mahasammelan.jpg"',
    'src="youth_vss_1786471607567.jpg"': 'src="images/youth_vss.jpg"',
    '<div class="dropdown-menu rich-menu" style="width: 450px;">': '<div class="dropdown-menu rich-menu">'
}

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Safely replaced image paths and inline styles.")
