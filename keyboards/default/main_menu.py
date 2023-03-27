# import markups
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



BUTTTON = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Qora ro'yxat"),
            KeyboardButton(text="📌 Yo'riqnoma")
        ],
        [
            KeyboardButton(text="👥 Guruh nazorati"),
        ],

    ],
    resize_keyboard=True,
    selective=True
    )