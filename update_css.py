import re

css_addition = """
/* -- Rich Dropdowns -- */
.nav__links li {
  position: relative;
}
.has-dropdown > a {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
.dropdown-icon {
  width: 14px;
  height: 14px;
  stroke: currentColor;
  stroke-width: 2;
  fill: none;
  transition: transform 0.2s ease;
}
.nav__links li:hover .dropdown-icon {
  transform: rotate(180deg);
}

.has-dropdown { position: static !important; }
.nav { position: sticky; }

.dropdown-menu.rich-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background: var(--white);
  width: 900px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.12);
  padding: 1.5rem;
  display: flex;
  gap: 2rem;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 100;
  border: 1px solid rgba(0,0,0,0.05);
}
.nav__links li:hover .dropdown-menu.rich-menu {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

.rich-menu__left {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.rich-menu__item {
  display: flex !important;
  align-items: center;
  gap: 1.25rem;
  padding: 1.25rem 1rem !important;
  border-bottom: 1px solid rgba(0,0,0,0.04);
  transition: background 0.3s !important;
  border-radius: 8px;
  text-decoration: none;
}
.rich-menu__item:last-child {
  border-bottom: none;
}
.rich-menu__item:hover {
  background: #faf7f2 !important;
}
.rich-menu__icon {
  width: 48px;
  height: 48px;
  background: #f4ede4;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--blue);
}
.rich-menu__icon svg {
  width: 22px;
  height: 22px;
  stroke: currentColor;
  stroke-width: 1.5;
  fill: none;
}
.rich-menu__text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}
.rich-menu__title {
  font-family: var(--ff-heading);
  font-size: 1.05rem;
  font-weight: 600;
  color: var(--blue);
}
.rich-menu__desc {
  font-size: 0.85rem;
  color: #4a5568;
  line-height: 1.4;
}
.rich-menu__arrow {
  width: 18px;
  height: 18px;
  stroke: var(--saffron);
  stroke-width: 2;
  fill: none;
  opacity: 0;
  transform: translateX(-10px);
  transition: all 0.3s;
}
.rich-menu__item:hover .rich-menu__arrow {
  opacity: 1;
  transform: translateX(0);
}

/* Featured Image Right Column */
.rich-menu__right {
  width: 350px;
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  flex-shrink: 0;
}
.rich-menu__right img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}
.rich-menu__right:hover img {
  transform: scale(1.05);
}
.rich-menu__overlay {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  background: var(--blue);
  border-radius: 8px;
  padding: 1.25rem;
  display: flex;
  gap: 1rem;
  color: white;
  align-items: center;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
.rich-menu__overlay-icon {
  width: 40px;
  height: 40px;
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.rich-menu__overlay-icon svg {
  width: 20px;
  height: 20px;
  stroke: white;
  stroke-width: 1.5;
  fill: none;
}
.rich-menu__overlay-text {
  font-size: 0.85rem;
  line-height: 1.4;
  font-weight: 400;
}
.rich-menu__overlay-text .line {
  display: block;
  width: 30px;
  height: 2px;
  background: var(--saffron);
  margin-top: 0.5rem;
}

/* Mega Menu variant for Programs */
.dropdown-menu.rich-menu.rich-menu--mega {
  width: 1100px; /* very wide for 3 columns */
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  padding: 2.5rem;
}
.rich-menu__mega-col h4 {
  font-family: var(--ff-heading);
  font-size: 1.1rem;
  color: var(--blue);
  margin-bottom: 1rem;
  padding-left: 1rem;
  position: relative;
}
.rich-menu__mega-col h4::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  bottom: 2px;
  width: 3px;
  background: var(--saffron);
  border-radius: 2px;
}
/* Re-use .rich-menu__item styling for mega items, but smaller padding */
.rich-menu__mega-col .rich-menu__item {
  padding: 1rem 0.75rem !important;
  gap: 1rem;
}
.rich-menu__mega-col .rich-menu__icon {
  width: 40px;
  height: 40px;
}
.rich-menu__mega-col .rich-menu__icon svg {
  width: 18px;
  height: 18px;
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'/\* -- Dropdowns -- \*/.*?/\* Drawer styles addition \*/', css_addition + '\n\n/* Drawer styles addition */', content, flags=re.DOTALL)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated style.css with Rich Dropdowns")
