/* ============================================================
   APSA — main.js
   Handles: Carousel · Nav scroll · Accordion · Tabs · Reveal
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Active nav link ── */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav__link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ── Sticky nav shadow ── */
  const nav = document.querySelector('.nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 10);
    }, { passive: true });
  }

  /* ── Mobile hamburger ── */
  const hamburger = document.querySelector('.nav__hamburger');
  const drawer = document.querySelector('.nav__drawer');
  if (hamburger && drawer) {
    hamburger.addEventListener('click', () => {
      const open = hamburger.classList.toggle('open');
      drawer.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    // Close on link click
    drawer.querySelectorAll('.nav__link').forEach(l => {
      l.addEventListener('click', () => {
        hamburger.classList.remove('open');
        drawer.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── Hero Carousel ── */
  const slidesWrapper = document.querySelector('.hero__slides');
  if (slidesWrapper) {
    const slides = Array.from(slidesWrapper.querySelectorAll('.hero__slide'));
    const dots = Array.from(document.querySelectorAll('.hero__dot'));
    const prevBtn = document.querySelector('.hero__arrow--prev');
    const nextBtn = document.querySelector('.hero__arrow--next');
    let current = 0;
    let timer;

    function goTo(idx) {
      slides[current].classList.remove('active');
      dots[current]?.classList.remove('active');
      current = (idx + slides.length) % slides.length;
      slides[current].classList.add('active');
      dots[current]?.classList.add('active');
      slidesWrapper.style.transform = `translateX(-${current * 100}%)`;
    }

    function startTimer() {
      clearInterval(timer);
      timer = setInterval(() => goTo(current + 1), 5500);
    }

    // Init
    slides[0].classList.add('active');
    dots[0]?.classList.add('active');
    startTimer();

    prevBtn?.addEventListener('click', () => { goTo(current - 1); startTimer(); });
    nextBtn?.addEventListener('click', () => { goTo(current + 1); startTimer(); });
    dots.forEach((dot, i) => dot.addEventListener('click', () => { goTo(i); startTimer(); }));

    // Swipe support
    let startX = 0;
    slidesWrapper.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, { passive: true });
    slidesWrapper.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 50) { goTo(dx < 0 ? current + 1 : current - 1); startTimer(); }
    });
  }

  /* ── Accordion ── */
  document.querySelectorAll('.acc-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.acc-item');
      const wasOpen = item.classList.contains('open');
      // Close all in same accordion
      trigger.closest('.niyam-accordion')
        ?.querySelectorAll('.acc-item')
        .forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });

  /* ── Tabs ── */
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const panel = btn.dataset.tab;
      const container = btn.closest('[data-tabs]') || document;
      container.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      container.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      container.querySelector(`[data-panel="${panel}"]`)?.classList.add('active');
    });
  });

  /* ── Calendar month filter ── */
  document.querySelectorAll('.cal-month').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.cal-month').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  /* ── Donation amount buttons ── */
  document.querySelectorAll('.amount-options').forEach(group => {
    group.querySelectorAll('.amount-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        group.querySelectorAll('.amount-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const customInput = group.closest('.donate-card')?.querySelector('.amount-custom');
        if (customInput) customInput.value = btn.textContent.replace('$', '').replace('Custom','');
      });
    });
  });

  /* ── Scroll reveal ── */
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(el => io.observe(el));
  }

  /* ── Samaj finder search ── */
  const finderInput = document.querySelector('.finder__input');
  if (finderInput) {
    finderInput.addEventListener('input', () => {
      const q = finderInput.value.toLowerCase();
      document.querySelectorAll('.samaj-tile').forEach(tile => {
        const name = tile.querySelector('.samaj-tile__name')?.textContent.toLowerCase() || '';
        const loc = tile.querySelector('.samaj-tile__loc')?.textContent.toLowerCase() || '';
        tile.style.display = (name.includes(q) || loc.includes(q)) ? '' : 'none';
      });
    });
  }

  /* ── Form submit feedback ── */
  document.querySelectorAll('form.ajax-form').forEach(form => {
    form.addEventListener('submit', e => {
      e.preventDefault();
      const btn = form.querySelector('[type="submit"]');
      const original = btn.textContent;
      btn.textContent = 'Sending…';
      btn.disabled = true;
      setTimeout(() => {
        btn.textContent = '✓ Sent!';
        setTimeout(() => { btn.textContent = original; btn.disabled = false; }, 2500);
      }, 1200);
    });
  });

});
