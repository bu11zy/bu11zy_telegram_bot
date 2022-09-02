#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from aiogram.dispatcher import FSMContext



#То что происходит после нажатия кнокпи "Выйти в главное меню"
@dp.callback_query_handler(text='main_menu', state='*')
async def admin_panel_main_menu_callback(callback_query: types.CallbackQuery, state: FSMContext):
    curr_state = await state.get_state()
    #Ничего не делать, если состояния нет
    if curr_state is None:
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Ваш ID: {callback_query.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)
    elif curr_state is not None:
        await state.finish()
        #Удаляем предидущее сообщение
        await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=callback_query.from_user.id,
                               text=f"Ваш ID: {callback_query.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)