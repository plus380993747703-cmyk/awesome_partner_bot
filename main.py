import asyncio
import threading
import os
from aiogram.types import BotCommand
from flask import Flask
from app.bot import bot, dp

# === Настройка команд бота ===
async def set_bot_commands():
    commands = [
        BotCommand(command="tech", description="🧩 Тех.специалист"),
        BotCommand(command="bot", description="⚙️ Telegram-BOT’s"),
        BotCommand(command="design", description="🎨 Design-решения"),
        BotCommand(command="text", description="📝 Текст из медиа"),
    ]
    await bot.set_my_commands(commands)

# === Запуск бота через поллинг ===
async def run_bot():
    await set_bot_commands()
    await dp.start_polling(bot)

# === Flask-сервер для Render ===
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Запускаем Flask в отдельном потоке
    threading.Thread(target=run_flask).start()
    
    # Запускаем aiogram бота
    asyncio.run(run_bot())
