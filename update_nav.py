import os
import re

navbar = """<!-- NAV -->
<nav class="nav" id="main-nav">
  <div class="container nav__inner">
    <a href="index.html" class="nav__brand">
      <div class="nav__logo-mark" style="font-size: 1.1rem; padding-bottom: 2px;">ओ३म्</div>
      <div>
        <div class="nav__brand-name">APSA</div>
        <div class="nav__brand-sub">Arya Pratinidhi Sabha of America</div>
      </div>
    </a>
    <ul class="nav__links" role="list">
      <li><a href="index.html"     class="nav__link">Home</a></li>
      <li><a href="about.html"     class="nav__link">About Us</a></li>
      <li><a href="programs.html"  class="nav__link">Programs</a></li>
      <li><a href="resources.html" class="nav__link">Vedic Resources</a></li>
      <li><a href="events.html"    class="nav__link">Events</a></li>
      <li><a href="news.html"      class="nav__link">News &amp; Publications</a></li>
      <li><a href="contact.html"   class="nav__link">Contact Us</a></li>
    </ul>
    <div class="nav__actions">
      <a href="about.html#directory" class="btn btn-outline btn-sm">Find a Samaj</a>
      <a href="donate.html" class="btn btn-primary btn-sm">Donate</a>
    </div>
    <button class="nav__hamburger" aria-label="Menu" id="hamburger">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile drawer -->
<div class="nav__drawer" id="nav-drawer">
  <a href="index.html"     class="nav__link">Home</a>
  <a href="about.html"     class="nav__link">About Us</a>
  <a href="programs.html"  class="nav__link">Programs</a>
  <a href="resources.html" class="nav__link">Vedic Resources</a>
  <a href="events.html"    class="nav__link">Events</a>
  <a href="news.html"      class="nav__link">News &amp; Publications</a>
  <a href="contact.html"   class="nav__link">Contact Us</a>
  <a href="about.html#directory" class="btn btn-outline btn-sm">Find a Samaj</a>
  <a href="donate.html" class="btn btn-primary btn-sm">Donate</a>
</div>"""

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace anything between <nav ...</nav> and the following <div class="nav__drawer"...</div>
    pattern = re.compile(r'<!--.*?Nav.*?-->\s*<nav.*?</nav>\s*(?:<!--.*?drawer.*?-->\s*)?<div class="nav__drawer".*?</div>', re.DOTALL | re.IGNORECASE)
    
    # Fallback pattern if comments are missing
    fallback_pattern = re.compile(r'<nav class="nav" id="main-nav">.*?</nav>\s*(?:<!--.*?-->\s*)?<div class="nav__drawer".*?</div>', re.DOTALL)

    if pattern.search(content):
        new_content = pattern.sub(navbar, content)
    elif fallback_pattern.search(content):
        new_content = fallback_pattern.sub(navbar, content)
    else:
        print(f"Could not find nav in {file}")
        continue
    
    # Add active class - fixing the logic to avoid replacing the wrong hrefs
    filename = os.path.basename(file)
    new_content = new_content.replace(f'href="{filename}"     class="nav__link"', f'href="{filename}"     class="nav__link active"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")
