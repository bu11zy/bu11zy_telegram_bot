#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from bd_handlers.change_post.get_post_name import get_post_name


#В этой функции записывается изменение название поста
@dp.message_handler(state=FSM_change_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        try:
            #SQL функция
            row = await get_post_name(int(message.text))
            data['post_id'] = str(message.text)
            #Переходим к следующему состоянию
            await FSM_change_post.next()
            #Отправляем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"ID записи: {message.text}\n"
                                   f"Имя записи: {row['post_name']}\n"
                                   f"Введите новое имя записи:\n",
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)
        #Ошибка если ничего не приходит из SQL функции
        except TypeError:
            await state.finish()
            #Отправляем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"ID записи: {message.text}\n"
                                   f"Ошибка. Нет такого ID записи\n"
                                   f"Попробуйте ещё раз\n",
                                   reply_markup=admin_panel_keyboard_back_to_main_menu)