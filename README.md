# 🛍️ NegotiMart — AI-Powered Fashion E-Commerce

> *Shop premium fashion and negotiate your own price with NOVA, our Claude-powered AI style advisor.*

---

## ✨ Features

- **AI Price Negotiation** — Powered by Claude API. Users negotiate with NOVA across up to 3 rounds.
- **Full E-Commerce Flow** — Browse → Product Detail → Cart → Checkout → Orders
- **User Authentication** — JWT-based register/login system with bcrypt password hashing
- **Admin Dashboard** — Full CRUD for products, view all orders and users, revenue stats
- **Luxury UI** — Dark editorial aesthetic with gold accents, custom cursor, smooth animations
- **Responsive Design** — Works on desktop, tablet, and mobile

---

## 📁 Project Structure

```
negotimart/
├── app.py                        # Flask entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── negotimart.db                 # SQLite database (auto-created on first run)
│
├── backend/
│   ├── models/
│   │   └── database.py           # SQLite schema + seed data
│   └── routes/
│       ├── auth.py               # /api/auth — register, login, me
│       ├── products.py           # /api/products — list, detail, categories
│       ├── negotiate.py          # /api/negotiate — AI negotiation engine ⭐
│       ├── orders.py             # /api/orders — create, my orders
│       └── admin.py              # /api/admin — stats, CRUD, users
│
├── templates/
│   ├── base.html                 # Base layout (navbar, chatbot widget, footer)
│   ├── index.html                # Homepage
│   ├── shop.html                 # Product listing
│   ├── product.html              # Product detail
│   ├── cart.html                 # Shopping cart
│   ├── checkout.html             # Checkout
│   ├── login.html                # Login
│   ├── register.html             # Register
│   ├── orders.html               # My orders
│   └── admin.html                # Admin dashboard
│
└── static/
    ├── css/
    │   └── main.css              # All styles
    └── js/
        └── core.js               # Auth, Cart, API, Chatbot, utilities
```

---

## 🚀 Setup & Run

### Step 1 — Clone or download the project
```bash
cd negotimart
```

### Step 2 — Create a virtual environment
```bash
python -m venv venv

# Activate:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables
```bash
cp .env.example .env
```
Open `.env` and fill in:
```env
ANTHROPIC_API_KEY=your_actual_api_key_here
SECRET_KEY=any-random-secret-string
JWT_SECRET=another-random-secret
```
Get your Anthropic API key from: https://console.anthropic.com

### Step 5 — Run the app
```bash
python app.py
```

Open your browser: **http://localhost:5000**

---

## 🔑 Default Admin Credentials

| Field    | Value                      |
|----------|---------------------------|
| Email    | admin@negotimart.com       |
| Password | admin123                   |

> ⚠️ Change the admin password after first login in production.

---

## 🤖 How AI Negotiation Works

1. User clicks **"Negotiate Price"** on any product
2. The chatbot widget opens, NOVA introduces herself
3. User makes an offer (e.g. "Can I get this for $60?")
4. Claude API is called with a custom system prompt that includes:
   - Product name, description, list price
   - A **hidden floor price** (set per product by admin)
   - Negotiation rules (max 3 rounds, max 25% off)
5. NOVA responds in character, either counter-offering or accepting
6. Accepted deals are added to cart at the negotiated price

### Negotiation Rules (Configurable in `negotiate.py`)
- Round 1: Up to 10% discount
- Round 2: Up to 18% discount
- Round 3 (final): Up to 25% discount
- Floor price is never revealed or crossed

---

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new user |
| POST | `/api/auth/login` | Login |
| GET | `/api/auth/me` | Get current user |
| GET | `/api/products/` | List products (search, filter, sort) |
| GET | `/api/products/:id` | Get single product |
| GET | `/api/products/categories` | Get all categories |
| GET | `/api/products/featured` | Get 4 random featured |
| POST | `/api/negotiate/start` | Start negotiation session |
| POST | `/api/negotiate/chat` | Send message to NOVA |
| POST | `/api/negotiate/accept` | Accept deal |
| POST | `/api/orders/` | Place order |
| GET | `/api/orders/my` | Get my orders |
| GET | `/api/admin/stats` | Dashboard stats (admin only) |
| GET | `/api/admin/products` | All products (admin only) |
| POST | `/api/admin/products` | Add product (admin only) |
| PUT | `/api/admin/products/:id` | Update product (admin only) |
| DELETE | `/api/admin/products/:id` | Deactivate product (admin only) |
| GET | `/api/admin/orders` | All orders (admin only) |
| GET | `/api/admin/users` | All users (admin only) |

---

## 🎨 Design System

- **Font Display**: Cormorant Garamond (editorial serif)
- **Font Body**: Raleway (clean sans-serif)
- **Font Mono**: DM Mono (labels and UI elements)
- **Primary Color**: `#c9a96e` (gold)
- **Background**: `#0a0a0a` (near-black)
- **Theme**: Luxury dark editorial with gold accents

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| Database | SQLite (via sqlite3) |
| Auth | JWT + bcrypt |
| AI | Anthropic Claude API |
| Frontend | Vanilla JS + Jinja2 templates |
| Styling | Custom CSS (no framework) |
| Icons | Font Awesome 6 |
| Fonts | Google Fonts |

---

## 🔒 Security Notes

- Passwords hashed with bcrypt
- JWT tokens with 7-day expiry
- Admin routes protected by role check
- Floor prices never exposed to frontend
- No real payment processing (demo only)

---

## 📝 License

MIT — Build freely, negotiate boldly.
