#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu

#Создание Машины состояний
class FSM_create_user_role_admin(StatesGroup):
    user_id = State()

#Колбэк с кнопки выбора роли
@dp.callback_query_handler(text='take_user_role_admin', state=None)
async def load_user_role_admin(callback_query: types.CallbackQuery):
    #Выбираем состояние
    await FSM_create_user_role_admin.user_id.set()
    #Отправляем сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Роль успешно выбрана.\n\nВведите user_id пользователя которого хотите назначить администратором:")

#Принимаем состояние
@dp.message_handler(state=FSM_create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем в дату указанный user_id в сообщении
    async with state.proxy() as data:
        data['user_id'] = message.text
    #Закрываем состояние    
    await state.finish()
    #Присылаем сообщение
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"\nАдминистратор\n"
                           f"ID пользователя:  {data['user_id']}\n"
                           f"\nУспешно создан",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)