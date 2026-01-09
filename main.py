import asyncio
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
from app.config import BOT_TOKEN
from app.handlers import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def health_check(request):
    return web.Response(text="Bot is alive")

async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="tech", description="🧩 Тех.специалист"),
        BotCommand(command="bot", description="⚙️ Telegram-BOT's"),
        BotCommand(command="design", description="🎨 Design-решения"),
        BotCommand(command="text", description="📝 Текст из медиа"),
    ]
    await bot.set_my_commands(commands)

async def run_bot():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()
    dp.include_router(router)
    
    await set_bot_commands(bot)
    logger.info("Bot started with long polling")
    
    await dp.start_polling(bot)

async def start_http_server():
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    await site.start()
    logger.info("HTTP server started on port 8080")
    return runner

async def main():
    # Запускаем HTTP-сервер в фоне
    http_runner = await start_http_server()
    
    # Запускаем бота
    try:
        await run_bot()
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        await http_runner.cleanup()

if __name__ == "__main__":
    asyncio.run(main())