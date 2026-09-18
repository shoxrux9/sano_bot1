import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

# Support ADMIN_IDS or ADMIN_ID (comma-separated list of Telegram IDs)
ADMIN_IDS_RAW: str = os.getenv("ADMIN_IDS", os.getenv("ADMIN_ID", "0"))
ADMIN_IDS: list[int] = [
    int(i.strip()) for i in ADMIN_IDS_RAW.split(",") if i.strip().isdigit()
]

DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./sano_books.db")

def is_admin(user_id: int) -> bool:
    """Check if a given user_id is in ADMIN_IDS list."""
    return user_id in ADMIN_IDS
