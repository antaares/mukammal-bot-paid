from aiogram.dispatcher.filters.state import StatesGroup, State




class AutoMessage(StatesGroup):
    GetAdvertisement = State()
    GetTime = State()
    zed = State()
    red = State()