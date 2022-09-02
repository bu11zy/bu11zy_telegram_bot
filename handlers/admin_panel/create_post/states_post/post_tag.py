from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post


#В этой функции записывается тег
@dp.message_handler(state=FSM_create_post.post_tag)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем в дату тег
    async with state.proxy() as data:
        data['post_tag'] = message.text
        #Переходим к следующему состоянию
        await FSM_create_post.next()
        #Отправляем сообщение
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID пользователя: {message.from_user.id}\n"
                               f"Имя записи: {data['post_name']}\n"
                               f"Описание записи: {data['post_disc']}\n"
                               f"Тэг записи: {data['post_tag']}\n"
                               f"Введите ссылку записи:\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)