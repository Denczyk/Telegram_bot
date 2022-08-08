from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5052103879:AAEp9s8QPtyyWURe8c2_kBiWqb2iF_DpM_Y'
port = 8080

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())