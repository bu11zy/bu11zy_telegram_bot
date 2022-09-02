#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from bd_handlers.user_role.delete_user_role import delete_user_role

class FSM_delete_role_from_user(StatesGroup):
    user_id = State()


#Колбэк с Админ клавиатуры на удаление роли
@dp.callback_query_handler(text='delete_role_from_user')
async def admin_panel_create_user_role(callback_query: types.CallbackQuery):
    await FSM_delete_role_from_user.user_id.set()
    await bot.delete_message(chat_id=callback_query.from_user.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Кому вы хотите снять роль?\n"
                           f"Напишите ID:",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)


@dp.message_handler(state=FSM_delete_role_from_user.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем в дату указанный user_id в сообщении
    async with state.proxy() as data:
        data['user_id'] = message.text
        #Записываем в дату в виде строки
        str_data = str(data['user_id'])
        try:
            #Проверка число ли стр_дата, если нет ValueError
            float(str_data)
            #Записываем в дату в виде числа
            int_data = int(str_data)
            #Проверка меньше ли инт_дата чем ноль, если нет else:
            if int_data < 0:
                #Закрываем состояние
                await state.finish()
                #Присылаем сообщение
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"\nОшибка ID пользователя не может быть отрицательным\n"
                                       f"ID пользователя:  {str_data}\n"
                                       f"\nПопробуйте снова",
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
            else:
                #Закрываем состояние
                await state.finish()
                #Вызываем bd_handler
                await delete_user_role(user_id=int_data)
                #Присылаем сообщение
                await bot.send_message(chat_id=message.from_user.id,
                                       text=f"\nC пользователя снята роль\n"
                                       f"ID пользователя:  {int_data}\n",
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
        except ValueError:
            #Закрываем состояние
            await state.finish()
            #Присылаем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"\nОшибка ID пользователя (Это не число)\n"
                                   f"ID пользователя:  {str_data}\n"
                                   f"\nПопробуйте снова",
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)