from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




BLACK_LIST = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="So'zlar", callback_data="black_list_words"),
            InlineKeyboardButton(text="So'z qo'shish", callback_data="black_list_add_word"),
            InlineKeyboardButton(text="So'z o'chirish", callback_data="black_list_delete_word"),
            InlineKeyboardButton(text="So'zlarni o'chirish", callback_data="black_list_delete_all_words"),
        ],
    ],
)