from aiogram.dispatcher.filters.state import StatesGroup, State


class BlackList(StatesGroup):
    add_word = State()
    delete_word = State()
    delete_words = State()