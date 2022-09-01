#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from bd_handlers.user_role.check_user_role import check_bd_user_role


#Хендлер реагирует на комманду старт.
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = int(message.from_user.id)
    check_user_role = await check_bd_user_role(user_id=user_id)
    if check_user_role == 'admin':
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}")