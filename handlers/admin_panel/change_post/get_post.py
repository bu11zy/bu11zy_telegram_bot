#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup

#машина состояний
class FSM_change_post(StatesGroup):
    post_id = State()
    post_name = State()
    post_disc = State()
    post_tag = State()
    post_link = State()


#То что происходит после нажатия кнокпи "Изменить пост"
@dp.callback_query_handler(text='change_post')
async def admin_panel_change_post_callback(callback_query: types.CallbackQuery):
    await FSM_change_post.post_id.set()
    #Удаляем предидущее сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    #Отправляем сообщение с клавиатурой
    await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Введите ID поста:",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)