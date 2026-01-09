import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN, PORT
from app.handlers import router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="tech", description="🧩 Тех.специалист"),
        BotCommand(command="bot", description="⚙️ Telegram-BOT's"),
        BotCommand(command="design", description="🎨 Design-решения"),
        BotCommand(command="text", description="📝 Текст из медиа"),
    ]
    await bot.set_my_commands(commands)

async def main():
    # Инициализация бота с явным указанием parse_mode
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    
    # Подключаем роутер
    dp.include_router(router)
    
    # Устанавливаем команды бота
    await set_bot_commands(bot)
    
    logger.info("Бот запущен на long polling")
    
    try:
        # Запускаем long polling
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())