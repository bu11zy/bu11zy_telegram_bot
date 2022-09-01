#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

#Отмена состояния
@dp.message_handler(state="*", commands='отмена')
async def cancel(message: types.Message, state: FSMContext):
    #Проверка текущего состояния
    curr_state = await state.get_state()
    #Ничего не делать, если состояния нет
    if curr_state is None:
        return
    #Завершаем состояние и присылаем себе сообщение об отмене
    await state.finish()
    await bot.delete_message(chat_id=message.from_user.id,
                             message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"\nОтмена успешна\n",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)