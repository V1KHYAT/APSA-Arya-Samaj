import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Icons
icon_bulb = '<svg viewBox="0 0 24 24"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>'
icon_book = '<svg viewBox="0 0 24 24"><path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>'
icon_users = '<svg viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>'
icon_building = '<svg viewBox="0 0 24 24"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>'
icon_arrow = '<svg class="rich-menu__arrow" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>'
icon_heart = '<svg viewBox="0 0 24 24"><path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>'

def create_item(href, title, desc, icon):
    return f'''
    <a href="{href}" class="rich-menu__item">
      <div class="rich-menu__icon">{icon}</div>
      <div class="rich-menu__text">
        <span class="rich-menu__title">{title}</span>
        <span class="rich-menu__desc">{desc}</span>
      </div>
      {icon_arrow}
    </a>'''

nav_html = f'''    <ul class="nav__links" role="list">
      <li><a href="index.html" class="nav__link">Home</a></li>
      
      <li class="has-dropdown">
        <a href="about.html" class="nav__link">About Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            {create_item('about.html#mission', 'Mission, Vision & History', 'Discover the founding principles and journey of APSA.', icon_bulb)}
            {create_item('about.html#niyams', 'Ten Niyams', 'The core guiding principles of the Arya Samaj.', icon_book)}
            {create_item('about.html#leadership', 'Leadership', 'Meet the dedicated team guiding our mission forward.', icon_users)}
            {create_item('about.html#governance', 'Constitution & Governance', 'Our organizational bylaws and commitment to transparency.', icon_building)}
          </div>
          <div class="rich-menu__right">
            <img src="swami_dayanand_1786472309965.jpg" alt="About Us">
            <div class="rich-menu__overlay">
              <div class="rich-menu__overlay-icon">{icon_heart}</div>
              <div class="rich-menu__overlay-text">
                Rooted in the Vedas.<br>Committed to humanity.
                <span class="line"></span>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="programs.html" class="nav__link">Programs <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu rich-menu--mega">
          <div class="rich-menu__mega-col">
            <h4>Education & Youth</h4>
            {create_item('programs.html#vss', 'Vedic Sanskriti Schools', 'Preserving heritage for the next generation.', icon_book)}
            {create_item('programs.html#vdat', 'Vedic Dharma Aptitude Test', 'Annual test to evaluate Vedic knowledge.', icon_bulb)}
            {create_item('programs.html#balwadi', 'Balwadi & Online Programs', 'Early childhood and remote learning.', icon_users)}
            {create_item('programs.html#vayu', 'VAYU', 'Vedic Arya Youth Umbrella initiatives.', icon_users)}
          </div>
          <div class="rich-menu__mega-col">
            <h4>Community & Wellness</h4>
            {create_item('programs.html#village', 'Vedic Village', 'A sanctuary for spiritual and communal living.', icon_building)}
            {create_item('programs.html#aham', 'AHAM', 'Mental health awareness and support.', icon_heart)}
            {create_item('programs.html#relief', 'Natural Disaster Relief', 'Seva and aid for communities in need.', icon_heart)}
            {create_item('programs.html#paropkaar', 'Paropkaar Foundation', 'Philanthropic initiatives for the greater good.', icon_bulb)}
          </div>
          <div class="rich-menu__mega-col">
            <h4>Growth & Networking</h4>
            {create_item('programs.html#new-samaj', 'Establishing a New Samaj', 'Guidelines for starting a local chapter.', icon_building)}
            {create_item('programs.html#apn', 'Arya Professional Network', 'Connecting professionals globally.', icon_users)}
            {create_item('programs.html#amf', 'Arya Matrimony Forum', 'A platform for meaningful Vedic connections.', icon_users)}
            {create_item('programs.html#vpt', 'Vedic Purohit Training', 'Training the next generation of scholars.', icon_book)}
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="resources.html" class="nav__link">Vedic Resources <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            {create_item('resources.html#library', 'Digital Library', 'Explore our collection of Vedas and literature.', icon_book)}
            {create_item('resources.html#practices', 'Daily Practices', 'Guides for Sandhya, Yajna, and daily Mantras.', icon_bulb)}
            {create_item('resources.html#audio', 'Audio & Audio-Visual Guides', 'Multimedia resources for learning.', icon_bulb)}
            {create_item('resources.html#purohit', 'Purohit Services', 'Request a Purohit for your ceremonies.', icon_users)}
          </div>
          <div class="rich-menu__right">
            <img src="hero_havan_1786471497788.jpg" alt="Resources">
            <div class="rich-menu__overlay">
              <div class="rich-menu__overlay-icon">{icon_book}</div>
              <div class="rich-menu__overlay-text">
                Spiritual growth.<br>Daily Vedic practices.
                <span class="line"></span>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="events.html" class="nav__link">Events <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            {create_item('events.html#calendar', 'Central Event Calendar', 'Stay updated with all upcoming activities.', icon_building)}
            {create_item('events.html#mahasammelan', 'Annual Arya Mahasammelan', 'Our flagship yearly gathering.', icon_users)}
            {create_item('events.html#webinars', 'Regional Webinars', 'Join virtual and local spiritual meetups.', icon_bulb)}
          </div>
          <div class="rich-menu__right">
            <img src="mahasammelan_1786472019430.jpg" alt="Events">
            <div class="rich-menu__overlay">
              <div class="rich-menu__overlay-icon">{icon_users}</div>
              <div class="rich-menu__overlay-text">
                Uniting communities.<br>Celebrating heritage.
                <span class="line"></span>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="news.html" class="nav__link">News <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            {create_item('news.html#navrang', 'Navrang Times Archive', 'Read our monthly magazine publications.', icon_book)}
            {create_item('news.html#publications', 'APSA Publications', 'Books, literature, and Annual Vedic Calendars.', icon_book)}
            {create_item('news.html#press', 'Press Releases', 'Official news and community updates.', icon_bulb)}
          </div>
          <div class="rich-menu__right">
            <img src="youth_vss_1786471607567.jpg" alt="News">
            <div class="rich-menu__overlay">
              <div class="rich-menu__overlay-icon">{icon_bulb}</div>
              <div class="rich-menu__overlay-text">
                Sharing knowledge.<br>Inspiring minds.
                <span class="line"></span>
              </div>
            </div>
          </div>
        </div>
      </li>

      <li class="has-dropdown">
        <a href="contact.html" class="nav__link">Contact Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu" style="width: 450px;">
          <div class="rich-menu__left">
            {create_item('contact.html#general', 'General Contact', 'Get in touch with our main office.', icon_users)}
            {create_item('contact.html#media', 'Media & Inquiries Form', 'For press, partnerships, and questions.', icon_bulb)}
          </div>
        </div>
      </li>
    </ul>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace desktop nav (we will replace everything from <ul class="nav__links" to </ul>
    content = re.sub(r'    <ul class="nav__links" role="list">.*?    </ul>', nav_html, content, flags=re.DOTALL)
    
    # Update cache versions
    content = re.sub(r'href="css/style\.css\?v=\d+"', 'href="css/style.css?v=3"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files for rich menu.")
