from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import types

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


from loader import dp, db

scheduler = AsyncIOScheduler()


async def start_service(data, user_id: int, delay_time: int):
    job_id = db.unique_id(user_id=user_id)
    if db.get_user_job(user_id=user_id):
        try:
            scheduler.remove_job(db.get_user_job(user_id=user_id))
        except Exception as e:
            pass
        db.delete_job_id(user_id=user_id)
    scheduler.add_job(service, trigger= 'interval', minutes=delay_time, id=job_id, max_instances=50, args=[data])
    db.add_job_id(user_id)
    try:
        scheduler.start()
    except Exception as e:
        pass

async def stop_service(user_id: int):
    if db.get_user_job(user_id=user_id):
        try:
            scheduler.remove_job(db.get_user_job(user_id=user_id))
        except Exception as e:
            pass
        db.delete_job_id(user_id=user_id)
        



async def service(message: types.Message):
    allgroups = db.get_groups_by_admin(message.from_user.id)
    for group in allgroups:
        try:
            await message.copy_to(group, reply_markup=message.reply_markup)
        except Exception as e:
            pass

