import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

desktop_nav_links = """    <ul class="nav__links" role="list">
      <li><a href="index.html" class="nav__link">Home</a></li>
      
      <li class="has-dropdown">
        <a href="about.html" class="nav__link">About Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu">
          <a href="about.html#mission">Mission, Vision & History</a>
          <a href="about.html#niyams">Ten Niyams</a>
          <a href="about.html#leadership">Leadership</a>
          <a href="about.html#governance">Constitution & Governance</a>
        </div>
      </li>

      <li class="has-dropdown has-mega">
        <a href="programs.html" class="nav__link">Programs <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu mega-menu">
          <div class="mega-col">
            <h4>Education & Youth</h4>
            <a href="programs.html#vss">Vedic Sanskriti Schools</a>
            <a href="programs.html#vdat">Vedic Dharma Aptitude Test</a>
            <a href="programs.html#balwadi">Balwadi & Online Programs</a>
            <a href="programs.html#vayu">VAYU</a>
          </div>
          <div class="mega-col">
            <h4>Community & Wellness</h4>
            <a href="programs.html#village">Vedic Village</a>
            <a href="programs.html#aham">AHAM</a>
            <a href="programs.html#relief">Natural Disaster Relief</a>
            <a href="programs.html#paropkaar">Paropkaar Foundation</a>
          </div>
          <div class="mega-col">
            <h4>Growth & Networking</h4>
            <a href="programs.html#new-samaj">Establishing a New Arya Samaj</a>
            <a href="programs.html#apn">Arya Professional Network</a>
            <a href="programs.html#amf">Arya Matrimony Forum</a>
            <a href="programs.html#vpt">Vedic Purohit Training</a>
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="resources.html" class="nav__link">Vedic Resources <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu">
          <a href="resources.html#library">Digital Library</a>
          <a href="resources.html#practices">Daily Practices</a>
          <a href="resources.html#audio">Audio & Audio-Visual Guides</a>
          <a href="resources.html#purohit">Purohit Services & Request Form</a>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="events.html" class="nav__link">Events <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu">
          <a href="events.html#calendar">Central Event Calendar</a>
          <a href="events.html#mahasammelan">Annual Arya Mahasammelan</a>
          <a href="events.html#webinars">Regional Webinars & Satsangs</a>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="news.html" class="nav__link">News & Publications <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu">
          <a href="news.html#navrang">Navrang Times Archive</a>
          <a href="news.html#publications">APSA Publications</a>
          <a href="news.html#press">Press Releases & Announcements</a>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="contact.html" class="nav__link">Contact Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu">
          <a href="contact.html#general">General Contact & Office Location</a>
          <a href="contact.html#media">Media & Inquiries Form</a>
        </div>
      </li>
    </ul>"""

drawer_html = """<!-- Mobile drawer -->
<div class="nav__drawer" id="nav-drawer">
  <a href="index.html" class="nav__link">Home</a>
  
  <div class="drawer-group">
    <a href="about.html" class="nav__link">About Us</a>
    <div class="drawer-sub">
      <a href="about.html#mission">Mission, Vision & History</a>
      <a href="about.html#niyams">Ten Niyams</a>
      <a href="about.html#leadership">Leadership</a>
      <a href="about.html#governance">Constitution & Governance</a>
    </div>
  </div>

  <div class="drawer-group">
    <a href="programs.html" class="nav__link">Programs</a>
    <div class="drawer-sub">
      <a href="programs.html#vss">Vedic Sanskriti Schools</a>
      <a href="programs.html#vdat">Vedic Dharma Aptitude Test</a>
      <a href="programs.html#balwadi">Balwadi & Online Programs</a>
      <a href="programs.html#vayu">VAYU</a>
      <a href="programs.html#village">Vedic Village</a>
      <a href="programs.html#aham">AHAM</a>
      <a href="programs.html#relief">Natural Disaster Relief</a>
      <a href="programs.html#paropkaar">Paropkaar Foundation</a>
      <a href="programs.html#new-samaj">Establishing a New Arya Samaj</a>
      <a href="programs.html#apn">Arya Professional Network</a>
      <a href="programs.html#amf">Arya Matrimony Forum</a>
      <a href="programs.html#vpt">Vedic Purohit Training</a>
    </div>
  </div>

  <div class="drawer-group">
    <a href="resources.html" class="nav__link">Vedic Resources</a>
    <div class="drawer-sub">
      <a href="resources.html#library">Digital Library</a>
      <a href="resources.html#practices">Daily Practices</a>
      <a href="resources.html#audio">Audio & Audio-Visual Guides</a>
      <a href="resources.html#purohit">Purohit Services & Request Form</a>
    </div>
  </div>

  <div class="drawer-group">
    <a href="events.html" class="nav__link">Events</a>
    <div class="drawer-sub">
      <a href="events.html#calendar">Central Event Calendar</a>
      <a href="events.html#mahasammelan">Annual Arya Mahasammelan</a>
      <a href="events.html#webinars">Regional Webinars & Satsangs</a>
    </div>
  </div>

  <div class="drawer-group">
    <a href="news.html" class="nav__link">News & Publications</a>
    <div class="drawer-sub">
      <a href="news.html#navrang">Navrang Times Archive</a>
      <a href="news.html#publications">APSA Publications</a>
      <a href="news.html#press">Press Releases & Announcements</a>
    </div>
  </div>

  <div class="drawer-group">
    <a href="contact.html" class="nav__link">Contact Us</a>
    <div class="drawer-sub">
      <a href="contact.html#general">General Contact & Office Location</a>
      <a href="contact.html#media">Media & Inquiries Form</a>
    </div>
  </div>

  <a href="about.html#directory" class="btn btn-outline btn-sm">Find a Samaj</a>
  <a href="donate.html" class="btn btn-primary btn-sm">Donate</a>
</div>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace desktop nav
    content = re.sub(r'    <ul class="nav__links" role="list">.*?    </ul>', desktop_nav_links, content, flags=re.DOTALL)
    
    # Replace drawer nav
    content = re.sub(r'<!-- Mobile drawer -->\s*<div class="nav__drawer" id="nav-drawer">.*?</div>', drawer_html, content, flags=re.DOTALL)
    
    # Update cache versions
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=2"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all HTML files.")
