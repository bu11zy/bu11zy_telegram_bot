#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post


#В этой функции записывается изменение название тега
@dp.message_handler(state=FSM_change_post.post_tag)
async def post_tag(message: types.Message, state: FSMContext):
    #Записываем в дату название тега
    async with state.proxy() as data:
        data['post_tag'] = str(message.text)
        #Переходим к следующему состоянию
        await FSM_change_post.next()
        #Отправляем сообщение
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID записи: {data['post_id']}\n"
                               f"Имя записи: {data['post_name']}\n"
                               f"Описание записи: {data['post_disc']}\n"
                               f"Новый тег: {data['post_tag']}\n"
                               f"Введите новую ссылку:\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)