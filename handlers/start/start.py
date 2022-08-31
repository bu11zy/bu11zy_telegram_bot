#Импорты
from aiogram import types
from config.bot_config import dp, bot, ADMIN
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu

#Хендлер реагирует на комманду старт.
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id == ADMIN:
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}")