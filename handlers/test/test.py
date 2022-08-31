#Импорты
from aiogram import types
from config.bot_config import dp


#Хендлер реагирует на любой текст и присылает вам ваше сообщение.
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)