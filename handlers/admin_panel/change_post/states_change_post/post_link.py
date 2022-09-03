#Импорты
from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.change_post.get_post import FSM_change_post
from bd_handlers.change_post.change_post import change_post
from bd_handlers.create_post.check_user_name import check_bd_user_name
import datetime


#В этой функции изменяется пост
@dp.message_handler(state=FSM_change_post.post_link)
async def post_link(message: types.Message, state: FSMContext):
    #Записываем в дату название поста
    async with state.proxy() as data:
        data['post_link'] = str(message.text)
        #Переходим к следующему состоянию
        post_name = str(data['post_name'])
        post_disc = str(data['post_disc'])
        post_tag = str(data['post_tag'])
        post_link = str(data['post_link'])
        post_id = int(data['post_id'])
        user_id = int(message.from_user.id)
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        #Закрываем состояние
        await state.finish()
        user_name = await check_bd_user_name(user_id=user_id)
        #SQL функция
        await change_post(post_name=post_name, post_disc=post_disc, post_tag=post_tag,
                          post_link=post_link, change_user_name=user_name, change_date=cur_date, change_time=cur_time, post_id=post_id)
        #Отправляем сообщение
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID записи: {post_id}\n"
                               f"Имя записи: {post_name}\n"
                               f"Описание записи: {post_disc}\n"
                               f"Тег записи: {post_tag}\n"
                               f"Новая ссылка: {post_link}\n"
                               f"Запись успешно изменена.\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)