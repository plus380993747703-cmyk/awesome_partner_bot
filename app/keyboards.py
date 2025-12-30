from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config import ADMIN_USERNAME

contact_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💬 Написать сообщение", url=f"https://t.me/{ADMIN_USERNAME}")]
])

tech_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🧩 Тех.специалист", callback_data="tech")]
])

bot_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⚙️ Telegram-BOT’s", callback_data="bot")]
])

design_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎨 Design-решения", callback_data="design")]
])

text_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Текст из медиа", callback_data="text")]
])

details_inline_map = {
    "tech": InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1️⃣ Разовые задачи (тех-помощь)", callback_data="tech_details")]
    ]),
    "text": InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Задачи / Сроки / Расценки", callback_data="text_details")]
    ]),
    "design": InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 Задачи / Сроки / Расценки", callback_data="design_details")]
    ]),
    "bot": contact_inline
}

text_details_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💬 Написать сообщение", url=f"https://t.me/{ADMIN_USERNAME}")],
    [InlineKeyboardButton(text="📝 Текст с изображений", callback_data="oсr_text")]
])

tech_step_2_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="2️⃣ Подготовка к запуску продукта", callback_data="tech_step_2")]
])

tech_step_3_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="3️⃣ Постоянный тех. специалист", callback_data="tech_step_3")]
])
