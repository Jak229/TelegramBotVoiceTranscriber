import asyncio
import logging
from dp import bot, dp
from api.main import users
from db.models import async_main
from api.admin.admin import admin

logging.basicConfig(level=logging.INFO)


# Main function to start the bot
async def main():
    """
    Entry point for starting the Telegram bot.

    Initializes the database, includes routers, and starts polling.

    Returns:
        None
    """
    await async_main()

    dp.include_routers(users, admin)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
