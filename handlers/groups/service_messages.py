from aiogram import types

from filters import IsGroup
from loader import dp, bot, db


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    
    me_ = await bot.get_me()
    me_id = me_.id
    admins_ = await message.chat.get_administrators()
    admins_dict = {admin.status:admin.user.id for admin in admins_}
    creator = admins_dict.get('creator')

    if me_id in [new.id for new in message.new_chat_members]:
        await message.answer("Bot guruhga qo'shildi!")
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        data = db.get_group(message.chat.id)

        if member.status == 'creator':
            if data and data[0] == message.from_user.id:
                await message.answer("Guruh sizniki!")
                return
            if data and data[0] != message.from_user.id:
                await message.answer("Guruh sizga biriktirildi!")
                db.update_group(message.chat.id, message.from_user.id)
                return
            await message.answer("Siz guruhning owner'siz!")
            db.add_group(message.chat.id, message.from_user.id)

        elif member.status == 'administrator':
            admins = await bot.get_chat_administrators(message.chat.id)
            if data and data[0] == message.from_user.id:
                if 'creator' in [admin.status for admin in admins]:
                    await message.answer("Siz guruhning superadmini emassiz!, Guruh superadminga biriktirildi!")
                    db.update_group(message.chat.id, creator)
                    return
            elif data and data[0] != message.from_user.id:
                await message.answer("Guruh boshqa adminniki!")
                return
            
            else:
                await message.answer("Siz guruhning adminisiz!")
                db.add_group(message.chat.id, message.from_user.id)
            # db.add_group(message.chat.id, message.from_user.id)

        else:
            await message.answer("Siz guruhning superadmini emassiz!")
    



@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    me_ = await bot.get_me()
    member = message.chat.get_member(me_.id)
    if member.is_chat_admin() == False:
        await message.answer("Guruhda admin emasman, iltimmos meni admin qiling!")
        return
    try:
        await message.delete()
    except:
        pass