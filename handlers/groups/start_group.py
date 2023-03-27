from aiogram import types

from filters.is_group import IsGroup

from loader import dp, db


from aiogram.utils.exceptions import ChatAdminRequired

    

@dp.message_handler(IsGroup(), commands="start")
async def bot_start(message: types.Message):
    User = message.from_user
    user = await message.chat.get_member(User.id)
    admins_ = await message.chat.get_administrators()
    admins_dict = {admin.status:admin.user.id for admin in admins_}
    creator = admins_dict.get('creator')
    admins = [admin.user.id for admin in admins_]


    if user.status != 'creator' and user.status != 'administrator':
        await message.answer("Siz guruhda admin emassiz! ")
        if creator is None:
            await message.answer("Botni guruhga ulash uchun admin /start buyrug'ini berishi kerak!")
            return
        return db.add_group(message.chat.id, creator)
    

    data =  db.get_group(message.chat.id) #return owner_id
    if data and data[0] == message.from_user.id:
        if 'creator' in admins and user.status == 'administrator':
            await message.answer("Guruh endi sizniki emas, guruh creatorga biriktirildi!")
            db.update_group(message.chat.id, creator)
            return
       
        await message.answer("Guruh sizniki!")  
        return
    

    if data and data[0] != User.id:
        if user.status == 'creator':
            await message.answer("Guruh sizningki!")
            db.update_group(message.chat.id, user.id)
            return
        await message.answer("Guruh boshqa adminniki!")
        return 



    await message.answer("Bot ishga tushdi! Bot admin bo'lmasa ishlamaydi.")
    admins = await dp.bot.get_chat_administrators(message.chat.id)
    admins_status = [admin.status for admin in admins]




    me_ = await dp.bot.get_me()
    me_id = me_.id
    member = await dp.bot.get_chat_member(message.chat.id, message.from_user.id)

    if member.status == 'creator':
        await message.answer("Siz guruhning ownerisiz!, Guruh sizga biriktirildi!")
        db.add_group(message.chat.id, message.from_user.id)

    elif member.status == 'administrator' and 'creator' in admins_status:
        await message.answer("Siz guruhning owneri emassiz! Guruh ownerga biriktirildi!")
        db.add_group(message.chat.id, creator)

    elif member.status == 'administrator':
        await message.answer("Siz guruhning adminisiz! Guruh sizga biriktirildi!")
        db.add_group(message.chat.id, message.from_user.id)

    else:
        await message.answer("Siz guruhning admini emassiz! Botni guruhga ulash uchun admin /start buyrug'ini berishi kerak!")