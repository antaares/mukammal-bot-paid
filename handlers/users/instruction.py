

from aiogram import types
from aiogram.dispatcher.filters.builtin import Text

from loader import dp





@dp.message_handler(Text(equals="📌 Yo'riqnoma"))
async def bot_start(message: types.Message):
    await message.answer("👮🏻‍♂️Guruhingizda ishlatish uchun foydali buyruqlar👇\n\n"\
                        "⤴️ Foydalanuvchini belgilab (reply) qilib:\n"\
                        "/ro ma'lum vaqt yoki butunlay yoza olmaslik rejimiga tushirish!\n"\
                        "/ro 5\n"\
                        "foydalanuvchini 5 minut yoza olmaslik rejimiga tushirish.\n"\
                        "/ro 15 so'kinish.\n"\
                        "nima uchun yozolmaslik rejimiga tushganinini ko'rsatish.\n"\
                        "/unro reply qilngan userdan cheklovlarni olib tashlaydi.\n\n"\
                        "/ban guruhdan chetlatish.\n"\
                        "/unban bandan chiqarish.\n"\
                        "/addword qora ro'yxatga so'z qo'shish. (Namuna: /addword reklama)\n"\
                        "/delword qora ro'yxatdan so'z olib tashlash. (Namuna: /delword reklama)\n"\
                        "/clear qora ro'yxatni tozalash.\n"\
                        "__________________\n"\
                        "🎛Avto habar bo'imi orqali guruhingizga siz belgilagan vaqtda reklama jo'natib turishingiz mumkin toki to'xtatmagungizgacha.\n"\
                        "__________________\n"\
                        "✉️Reklama yuborish - sizni guruhlaringiz soni ko'p bo'lsa bot orqali bir vaqtni o'zida barcha guruhingizga reklama yuborishingzi mumkin.\n"\
                        "__________________\n"\
                        "📧Pin reklama - yuborgan reklamangizni guruhlaringizga pin qilib beradi.\n"
    )



