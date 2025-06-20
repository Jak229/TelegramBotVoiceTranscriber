from config.config import TOKEN
from aiogram import Dispatcher, Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

st = MemoryStorage()

# Initialize the bot with the token and set default parse mode to HTML
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode("HTML")))

# Create the main dispatcher for handling updates
dp = Dispatcher()
