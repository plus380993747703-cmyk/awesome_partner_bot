from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.handlers import router

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(router)
