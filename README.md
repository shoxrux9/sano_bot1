# 📚 SANO BOOKS — Telegram E-Commerce Bot

Professional, clean, and scalable Telegram e-commerce bot for **SANO BOOKS** publishing company built with **Python 3.11+**, **aiogram 3.x**, **SQLAlchemy (Async)**, and **SQLite**.

---

## 📁 Project Structure

```
sano_books_bot/
│
├── bot.py                # Main entrypoint, dispatcher & polling startup
├── config.py             # Environment variables and admin checker
├── requirements.txt      # Project dependencies
├── .env.example          # Template for environment variables
├── README.md             # Setup and usage guide
│
├── database/             # Database package (SQLAlchemy Async ORM)
│   ├── __init__.py
│   ├── db.py             # Async database engine & session maker
│   ├── models.py         # DB Schemas: User, Category, Book, CartItem, Order, OrderItem
│   └── crud.py           # Database CRUD queries & business logic
│
├── handlers/             # Bot interaction handlers (Routers)
│   ├── __init__.py       # Main router aggregator
│   ├── start.py          # /start command & main menu navigation
│   ├── books.py          # Category browsing, Bestsellers, New books & Book details
│   ├── search.py         # Book/author title search with FSM
│   ├── cart.py           # Persistent shopping cart management (add, edit, delete, clear)
│   ├── orders.py         # Multi-step checkout flow, Admin alerts & Customer order history
│   └── admin.py          # Admin panel (/admin), book CRUD, category CRUD & statistics
│
├── keyboards/            # Keyboard builders (Uzbek Latin UI)
│   ├── __init__.py
│   ├── inline.py         # Dynamic inline keyboards
│   └── reply.py          # Main navigation reply keyboards
│
├── states/               # Finite State Machine definitions
│   ├── __init__.py
│   └── states.py         # States for search, order checkout & admin CRUD
│
├── utils/                # Utility helpers
│   ├── __init__.py
│   └── helpers.py        # Currency formatters, order formatters & text utils
│
└── data/                 # Seed data
    └── seed.py           # Populates initial categories and demo SANO BOOKS titles
```

---

## 🚀 Quick Setup & Installation Guide

### 1. Prerequisites
- **Python 3.11 or higher** installed on your system.

### 2. Create Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration Setup

### 1. Create `.env` file
Copy the `.env.example` file to create your `.env` configuration file:

**Windows:**
```powershell
copy .env.example .env
```

**Mac / Linux:**
```bash
cp .env.example .env
```

### 2. How to get your `BOT_TOKEN`
1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Send `/newbot` and follow instructions to choose a bot name and username.
3. BotFather will provide an HTTP API token (e.g. `123456789:ABCdefGHIjklMNOpqrsTUVwxyZ`).
4. Copy this token into your `.env` file for `BOT_TOKEN`.

### 3. How to find your `ADMIN_ID`
1. Open Telegram and search for [@userinfobot](https://t.me/userinfobot) or [@raw_data_bot](https://t.me/raw_data_bot).
2. Press `/start` or send any message.
3. The bot will display your numerical Telegram `Id` (e.g. `123456789`).
4. Paste your numeric Telegram ID into `.env` for `ADMIN_ID`.

Example `.env` file:
```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyZ
ADMIN_ID=123456789
DATABASE_URL=sqlite+aiosqlite:///./sano_books.db
```

---

## 🏃 Running the Bot

Start the bot with:
```bash
python bot.py
```

The database tables will automatically be created and initial demo categories/books populated from `data/seed.py`.

---

## ✏️ Customization & Editing

### How to edit book data:
- **Interactive (Recommended)**: Send `/admin` inside Telegram as the admin user. You can add new books (`➕ Kitob qo‘shish`), edit, or delete them directly from Telegram!
- **Code Seed**: Open [data/seed.py](file:///c:/Users/user/Desktop/sano%20boot/data/seed.py) and modify `DEMO_BOOKS` array with real SANO BOOKS titles, prices, descriptions, and categories.

### How to change company name and text:
- **Bot Title & Welcome text**: Open [handlers/start.py](file:///c:/Users/user/Desktop/sano%20boot/handlers/start.py) and edit `cmd_start` or `about_us` text.
- **Header & Formatting**: Open [utils/helpers.py](file:///c:/Users/user/Desktop/sano%20boot/utils/helpers.py) to customize price symbols (`so‘m`), badge emojis, or order formats.

---

## 🛡️ Security & Clean Architecture
- Secrets (`BOT_TOKEN`, `ADMIN_ID`) are read exclusively from environment variables via `python-dotenv`.
- Admin commands and callbacks check `config.is_admin(user_id)` before execution.
- Separated database layer (`crud.py`) allows easy migration to **FastAPI**, **PostgreSQL**, **Web apps**, or **Mobile apps** in the future.
