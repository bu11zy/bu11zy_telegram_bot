#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup



class FSM_create_post(StatesGroup):
    post_name = State()
    post_disc = State()
    post_tag = State()
    post_link = State()


#То что происходит после нажатия кнокпи "Создать пост"
@dp.callback_query_handler(text='create_post')
async def admin_panel_create_post_callback(callback_query: types.CallbackQuery):
    await FSM_create_post.post_name.set()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Введите название записи:",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)