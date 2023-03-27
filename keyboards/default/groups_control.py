from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




BUTTTON_AUTO = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Reklama qo'shish"),
            KeyboardButton(text="❌ Reklama o'chirish"),
        ],
    ],
    resize_keyboard=True,
    selective=True
    )