#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_take_user_role import admin_panel_keyboard_take_user_role

#Колбэк с Админ клавиатуры на создание роли
@dp.callback_query_handler(text='make_user_role')
#Отправляем сообщение
async def admin_panel_create_user_role(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Кого вы хотите добавить?",
                           reply_markup=admin_panel_keyboard_take_user_role)