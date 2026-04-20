// ── NAVBAR SCROLL ──
const navbar = document.querySelector('.navbar');
const ham = document.querySelector('.nav-ham');
const navMenu = document.querySelector('.nav-menu');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
});

if (ham) {
  ham.addEventListener('click', () => {
    ham.classList.toggle('open');
    navMenu.classList.toggle('open');
  });
}

document.querySelectorAll('.nav-link, .dd-menu a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('open');
    ham && ham.classList.remove('open');
  });
});

// ── SCROLL REVEAL ──
const revealEls = document.querySelectorAll('.reveal');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 80);
      revealObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
revealEls.forEach(el => revealObs.observe(el));

// ── COUNTER ANIMATION ──
function animateCounter(el) {
  const target = parseInt(el.dataset.count);
  const suffix = el.dataset.suffix || '';
  const dur = 1800;
  const step = target / (dur / 16);
  let current = 0;
  const t = setInterval(() => {
    current += step;
    if (current >= target) { current = target; clearInterval(t); }
    el.textContent = Math.floor(current) + suffix;
  }, 16);
}
const counters = document.querySelectorAll('.stat-num[data-count]');
const counterObs = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounter(entry.target);
      counterObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });
counters.forEach(el => counterObs.observe(el));

// ── ACTIVE NAV ──
const path = window.location.pathname;
document.querySelectorAll('.nav-link[href]').forEach(link => {
  const href = link.getAttribute('href');
  if (href === '/' && path === '/') link.classList.add('active');
  else if (href !== '/' && path.startsWith(href)) link.classList.add('active');
});

// ── SPLASH ──
const splash = document.getElementById('splash');
if (splash) {
  setTimeout(() => { splash.style.display = 'none'; }, 3100);
}
