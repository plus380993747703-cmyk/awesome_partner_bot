from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from app.utils import load_text
from app.keyboards import (
    tech_inline,
    bot_inline,
    design_inline,
    text_inline,
    contact_inline,
    details_inline_map,
    tech_step_2_inline,
    tech_step_3_inline,
    text_details_inline
)

router = Router()

ASSETS_MAP = {
    "tech": "assets/getcourse.jpg",
    "text": "assets/whisper.jpg",
    "bot": "assets/bot.jpg",
    "design": "assets/design.jpg"
}

CAPTION_MAP = {
    "tech": "tech_caption",
    "text": "text_work_caption",
    "bot": "bot_caption",
    "design": "design_caption"
}

# --- START ---
@router.message(F.text == "/start")
async def start(message):
    await message.answer(load_text("main_tech"), reply_markup=tech_inline, parse_mode="HTML")
    await message.answer(load_text("main_bot"), reply_markup=bot_inline, parse_mode="HTML")
    await message.answer(load_text("main_design"), reply_markup=design_inline, parse_mode="HTML")
    await message.answer(load_text("main_whisper"), reply_markup=text_inline, parse_mode="HTML")

# --- Универсальная отправка услуги ---
async def send_service_common(message, key):
    await message.answer_photo(
        FSInputFile(ASSETS_MAP[key]),
        caption=load_text(CAPTION_MAP[key]),
        reply_markup=details_inline_map[key],
        parse_mode="HTML",
        protect_content=True
    )

# --- CALLBACK услуги ---
@router.callback_query(F.data.in_(["tech", "text", "bot", "design"]))
async def send_service_callback(callback: CallbackQuery):
    await send_service_common(callback.message, callback.data)
    await callback.answer()

# --- КОМАНДЫ (дубликаты кнопок) ---
@router.message(F.text == "/tech")
async def cmd_tech(message):
    await send_service_common(message, "tech")

@router.message(F.text == "/bot")
async def cmd_bot(message):
    await send_service_common(message, "bot")

@router.message(F.text == "/design")
async def cmd_design(message):
    await send_service_common(message, "design")

@router.message(F.text == "/text")
async def cmd_text(message):
    await send_service_common(message, "text")

# --- Text: задачи ---
@router.callback_query(F.data == "text_details")
async def send_text_details(callback: CallbackQuery):
    await callback.message.answer(
        load_text("text_work"),
        reply_markup=text_details_inline,
        parse_mode="HTML"
    )
    await callback.answer()

# --- OCR ---
@router.callback_query(F.data == "osr_text")
async def send_osr_text(callback: CallbackQuery):
    await callback.message.answer(
        load_text("osr"),
        reply_markup=contact_inline,
        parse_mode="HTML"
    )
    await callback.answer()

# --- Design / Bot ---
@router.callback_query(F.data.in_(["design_details", "bot_details"]))
async def send_details(callback: CallbackQuery):
    text_key = "design" if callback.data == "design_details" else "bot"
    await callback.message.answer(
        load_text(text_key),
        reply_markup=contact_inline,
        parse_mode="HTML"
    )
    await callback.answer()

# --- Tech steps ---
@router.callback_query(F.data == "tech_details")
async def send_tech_step_1(callback: CallbackQuery):
    await callback.message.answer(load_text("tech"), reply_markup=tech_step_2_inline, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "tech_step_2")
async def send_tech_step_2(callback: CallbackQuery):
    await callback.message.answer(load_text("tech2"), reply_markup=tech_step_3_inline, parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "tech_step_3")
async def send_tech_step_3(callback: CallbackQuery):
    await callback.message.answer(load_text("tech3"), reply_markup=contact_inline, parse_mode="HTML")
    await callback.answer()