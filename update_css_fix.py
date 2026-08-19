import re

css_addition = """
/* -- Rich Dropdowns -- */
.nav {
  position: relative; /* Make sure dropdowns are positioned relative to nav */
}
.nav__links {
  position: static;
}
.nav__links li {
  position: static; /* Force static so absolute positioned children break out */
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
  z-index: 1000; /* Ensure high z-index */
  border: 1px solid rgba(0,0,0,0.05);
}
.nav__links li:hover .dropdown-menu.rich-menu {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'/\* Fix Dropdown Positioning and Reset \*/.*?\.nav__links li:hover \.dropdown-menu\.rich-menu \{\s*opacity: 1;\s*visibility: visible;\s*transform: translateY\(0\);\s*\}', css_addition, content, flags=re.DOTALL)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed dropdown overlapping issue")
