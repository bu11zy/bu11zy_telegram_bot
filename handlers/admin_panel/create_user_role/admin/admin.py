#Импорты
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from bd_handlers.user_role.create_admin import create_admin
from bd_handlers.user_role.check_user_role import check_bd_user_role


#Создание Машины состояний
class FSM_create_user_role_admin(StatesGroup):
    user_id = State()
    user_name = State()


#Колбэк с кнопки выбора роли
@dp.callback_query_handler(text='take_user_role_admin', state=None)
async def load_user_role_admin(callback_query: types.CallbackQuery):
    #Выбираем состояние
    await FSM_create_user_role_admin.user_id.set()
    #Отправляем сообщение
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f"Роль успешно выбрана.\n\nВведите user_id пользователя которого хотите назначить администратором:",
                           reply_markup=admin_panel_keyboard_back_to_main_menu)


#Принимаем состояние
@dp.message_handler(state=FSM_create_user_role_admin.user_id)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем в дату указанный user_id в сообщении
    try:
        #Проверка число ли message.text, если нет ValueError
        float(message.text)
        test = await check_bd_user_role(user_id=int(message.text))
        if test == 'admin':
            await state.finish()
            #Присылаем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"\nОшибка ID пользователя уже используется"
                               f"\nЭто Админ\n"
                               f"\nID пользователя:  {message.text}\n"
                               f"\nПопробуйте снова",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
        elif test == 'cm':
            await state.finish()
            #Присылаем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"\nОшибка ID пользователя уже используется"
                               f"\nЭто Контент менеджер\n"
                               f"\nID пользователя:  {message.text}\n"
                               f"\nПопробуйте снова",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
        else:
            async with state.proxy() as data:
                data['user_id'] = message.text
                #Записываем в дату в виде строки
                str_data = str(data['user_id'])
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
                    await FSM_create_user_role_admin.next()
                    #Присылаем сообщение
                    await bot.send_message(chat_id=message.from_user.id,
                                           text=f"\nАдминистратор\n"
                                           f"ID пользователя:  {int_data}\n"
                                           f"\nВведите Никнейм: ",
                                           reply_markup=admin_panel_keyboard_back_to_main_menu)
    except ValueError:
        #Закрываем состояние
        await state.finish()
        #Присылаем сообщение
        await bot.send_message(chat_id=message.from_user.id,
                                       text=f"\nОшибка ID пользователя (Это не число)\n"
                                       f"ID пользователя:  {message.text}\n"
                                       f"\nПопробуйте снова",
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
            

@dp.message_handler(state=FSM_create_user_role_admin.user_name)
async def load_user_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        #Проверяем строка ли наше сообщение
        res = isinstance(message.text, str)
        if res is True:
            #Записываем в дату указанный user_name в сообщении
            data['user_name'] = message.text
            int_data_user_id = int(data['user_id'])
            await state.finish()
            #Вызываем наш bd_handler
            await create_admin(user_id=int_data_user_id, user_name=data['user_name'])
            #Присылаем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                       text=f"\nАдминистратор\n"
                                       f"ID пользователя:  {int_data_user_id}\n"
                                       f"Имя пользователя:  {data['user_name']}\n"
                                       f"\nРоль админа успешно присвоена.",
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)
        else:
            await state.finish()
            #Присылаем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                       text=f"\nОшибка вы прислали не строку\n"
                                       f"ID пользователя:  {data['user_id']}\n"
                                       f"Имя пользователя:  {message.text}\n"
                                       f"\nПопробуйте ещё раз",
                                       reply_markup=admin_panel_keyboard_back_to_main_menu)