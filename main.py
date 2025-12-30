import asyncio
from aiogram.types import BotCommand
from app.bot import bot, dp

async def set_bot_commands():
    commands = [
        BotCommand(command="tech", description="🧩 Тех.специалист"),
        BotCommand(command="bot", description="⚙️ Telegram-BOT’s"),
        BotCommand(command="design", description="🎨 Design-решения"),
        BotCommand(command="text", description="📝 Текст из медиа"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_bot_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
