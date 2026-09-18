import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import TelegramObject

import config
from database.db import init_db, AsyncSessionLocal
from data.seed import seed_data
from handlers import main_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class DbSessionMiddleware(BaseMiddleware):
    """Injects async SQLAlchemy session into every update handler data."""
    async def __call__(self, handler, event: TelegramObject, data: dict):
        async with AsyncSessionLocal() as session:
            data["session"] = session
            return await handler(event, data)

async def main():
    if not config.BOT_TOKEN:
        logger.error("❌ BOT_TOKEN environment variable is missing in .env file!")
        print("\n[XATOLIK] BOT_TOKEN sozlanmagan. Iltimos, .env faylini to'ldiring!\n")
        return

    logger.info("Initializing database...")
    await init_db()
    
    logger.info("Seeding initial data if needed...")
    try:
        await seed_data()
    except Exception as e:
        logger.warning(f"Seed data error or already seeded: {e}")

    # Create Bot & Dispatcher instances
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Register session middleware
    dp.update.middleware(DbSessionMiddleware())

    # Include main router
    dp.include_router(main_router)

    logger.info("🚀 SANO BOOKS Telegram Bot successfully started!")
    print("\n=======================================================")
    print(" 📚 SANO BOOKS Telegram Bot ishga tushdi!")
    print(f" 👑 Admin ID: {config.ADMIN_IDS}")
    print("=======================================================\n")

    try:
        # Delete webhook and start polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Bot crash error: {e}", exc_info=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped by user.")
