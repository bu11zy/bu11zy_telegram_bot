from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.create_post.create_post import FSM_create_post
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values
from bd_handlers.create_post.create_post import create_post
from bd_handlers.create_post.check_user_name import check_bd_user_name
import datetime


#Файл с конфигами
config = dotenv_values(CONFIG_DIR / '.env')
chat_id = str(config['chat_id'])


#В этой функции отправляется запрос в БД и создается запись в канале
@dp.message_handler(state=FSM_create_post.post_link)
async def load_user_id(message: types.Message, state: FSMContext):
    #Записываем ссылку в дату
    async with state.proxy() as data:
        data['post_link'] = message.text
        #Закрываем состояние
        await state.finish()
        #вывод данных в нужных нам типах
        user_id = int(message.from_user.id)
        post_name = str(data['post_name'])
        post_disc = str(data['post_disc'])
        post_tag = str(data['post_tag'])
        post_link = str(data['post_link'])
        cur_date = str(datetime.datetime.now().date())
        cur_time = str(datetime.datetime.now().time().replace(microsecond=0))
        #sql функция
        user_name = await check_bd_user_name(user_id=user_id)
        #sql функция
        await create_post(post_name=post_name, post_disc=post_disc, post_tag=post_tag, post_link=post_link,
                          user_name=user_name, create_data=cur_date, create_time=cur_time)
        #Отправляем сообщение себе в бота
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"ID пользователя:\n{message.from_user.id}\n"
                               f"Имя записи:\n{post_name}\n"
                               f"Описание записи:\n{post_disc}\n"
                               f"Тэг записи:\n#{post_tag}\n"
                               f"Ссылка записи:\n{post_link}\n"
                               f"Создано:\n{user_name}\n"
                               f"Дата создания:\n{cur_date}\n"
                               f"Время создания создания:\n{cur_time}\n"
                               f"Вы успешно создали запись\n",
                               reply_markup=admin_panel_keyboard_back_to_main_menu)
        #Отправляем сообщение в канал
        await bot.send_message(chat_id=chat_id,
                               text=f"<b>Название:</b>\n<i>{post_name}</i>\n"
                               f"\n<b>Описание:</b>\n<i>{post_disc}</i>\n"
                               f"\n<b>Ссылка:</b>\n<i>{post_link}</i>\n"
                               f"\n<b>Тэг:</b>\n<i>#{post_tag}</i>\n", parse_mode='HTML')
        