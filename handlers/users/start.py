from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.is_private import IsPrivate

from keyboards.default.main_menu import BUTTTON

from loader import dp, db 


@dp.message_handler(IsPrivate(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("👮🏻‍♂GURUH - da sizga yordam beraman👇\n"\
                        "🖇 - Reklama havolalarini tozalayman \n"\
                        "🔞 - Soʻkingan xabarlarni o‘chiraman \n"\
                        "🚫 - Spam xabarlarni tozalayman \n"\
                        "🗑 - Kirdi-chiqdilarni tozalayman",
                        reply_markup=BUTTTON)
    
    db.add_user(message.from_user.id, message.from_user.full_name)



@dp.message_handler(IsPrivate(), commands="error")
async def error(message: types.Message):
    await message.answer_document(document=open("logfile_err.log", "rb"))