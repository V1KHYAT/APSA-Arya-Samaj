import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

old_contact = """      <li class="has-dropdown">
        <a href="contact.html" class="nav__link">Contact Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            
    <a href="contact.html#general" class="rich-menu__item">
      <div class="rich-menu__icon"><svg viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg></div>
      <div class="rich-menu__text">
        <span class="rich-menu__title">General Contact</span>
        <span class="rich-menu__desc">Get in touch with our main office.</span>
      </div>
      <svg class="rich-menu__arrow" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>
    </a>
            
    <a href="contact.html#media" class="rich-menu__item">
      <div class="rich-menu__icon"><svg viewBox="0 0 24 24"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg></div>
      <div class="rich-menu__text">
        <span class="rich-menu__title">Media & Inquiries Form</span>
        <span class="rich-menu__desc">For press, partnerships, and questions.</span>
      </div>
      <svg class="rich-menu__arrow" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>
    </a>
          </div>
        </div>
      </li>"""

new_contact = """      <li class="has-dropdown">
        <a href="contact.html" class="nav__link">Contact Us <svg class="dropdown-icon" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
        <div class="dropdown-menu rich-menu">
          <div class="rich-menu__left">
            
    <a href="contact.html#general" class="rich-menu__item">
      <div class="rich-menu__icon"><svg viewBox="0 0 24 24"><path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg></div>
      <div class="rich-menu__text">
        <span class="rich-menu__title">General Contact</span>
        <span class="rich-menu__desc">Get in touch with our main office.</span>
      </div>
      <svg class="rich-menu__arrow" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>
    </a>
            
    <a href="contact.html#media" class="rich-menu__item">
      <div class="rich-menu__icon"><svg viewBox="0 0 24 24"><path d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg></div>
      <div class="rich-menu__text">
        <span class="rich-menu__title">Media & Inquiries Form</span>
        <span class="rich-menu__desc">For press, partnerships, and questions.</span>
      </div>
      <svg class="rich-menu__arrow" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>
    </a>
          </div>
          <div class="rich-menu__right">
            <img src="images/youth_vss.jpg" alt="Contact Us">
            <div class="rich-menu__overlay">
              <div class="rich-menu__overlay-icon"><svg viewBox="0 0 24 24"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg></div>
              <div class="rich-menu__overlay-text">
                Reach out today.<br>We are here to help.
                <span class="line"></span>
              </div>
            </div>
          </div>
        </div>
      </li>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_contact, new_contact)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated Contact Us dropdown with image.")
