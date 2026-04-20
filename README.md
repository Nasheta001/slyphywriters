# SlyphyWriters — Django Content Agency Website

A fully functional Django website for SlyphyWriters, a premium content agency 
specialising in iGaming, Fintech, and Crypto copywriting.

---

## 🚀 Setup (5 steps)

### 1. Create virtual environment
```bash
python -m venv venv

# Activate:
# Windows:   venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Apply database
```bash
python manage.py migrate
```

### 4. Create admin account
```bash
python manage.py createsuperuser
```

### 5. Run
```bash
python manage.py runserver
```

Open: **http://127.0.0.1:8000/**
Admin: **http://127.0.0.1:8000/admin/**  
Default login: `admin` / `admin123` (change immediately!)

---

## 📄 Pages & URLs

| Page | URL |
|------|-----|
| Home | / |
| About | /about/ |
| Process | /process/ |
| Services | /services/ |
| SEO Content Writing | /services/seo-content-writing/ |
| SEO Services | /services/seo-services/ |
| Translation | /services/translation/ |
| Editing | /services/editing/ |
| Link Building | /services/link-building/ |
| iGaming | /industry/igaming/ |
| Fintech | /industry/fintech/ |
| Crypto | /industry/crypto/ |
| Blog | /blog/ |
| Blog Post | /blog/<slug>/ |
| Contact | /contact/ |
| Get a Quote | /quote/ |
| Admin | /admin/ |

---

## 📝 Blog CMS

Go to `/admin/` → Blog → Posts → Add Post

- Set **Status** to `Published` for the post to appear on the site
- Add **Categories** to enable filtering
- Supports featured images (upload in admin)
- Rich content via the `content` field (plain text, HTML works too)

---

## 📬 Quote & Contact

All form submissions are saved to the database and visible in:
- `/admin/core/quoterequest/` — Quote requests
- `/admin/core/contactmessage/` — Contact messages

Mark as read directly from the admin list view.

---

## 🎨 Design Features

- Liquid glass navbar (transparent + blur + shimmer animation)
- Splash screen animation on homepage load
- Floating orb background animations (hero section)
- Scrolling marquee ticker
- Scroll-reveal animations on all cards
- Animated number counters (stats section)
- Dropdown menus with glass morphism
- Mobile hamburger menu
- Fully responsive (mobile, tablet, desktop)

---

## 🔧 Customisation

- **Colors**: Edit CSS variables in `static/css/style.css` (`:root` block)
- **Content**: All page text is in `templates/core/` — edit directly
- **Brand name**: Search & replace "SlyphyWriters" across templates
- **Contact email**: Update in `templates/core/contact.html`
- **Social links**: Update in `templates/base.html` (footer section)
