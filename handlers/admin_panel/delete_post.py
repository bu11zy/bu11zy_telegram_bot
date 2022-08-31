#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu


#То что происходит после нажатия кнокпи "Удалить пост"
@dp.callback_query_handler(text='delete_post')
async def admin_panel_delete_post_callback(callback_query: types.CallbackQuery):
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Тут будет удаляться пост",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)