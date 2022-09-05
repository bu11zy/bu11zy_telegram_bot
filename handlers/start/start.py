#Импорты
from aiogram import types
from config.bot_config import dp, bot
from keyboards.admin_panel_keyboard_main_menu import admin_panel_keyboard_main_menu
from keyboards.cm_keyboard_main_menu import cm_keyboard_main_menu
from bd_handlers.user_role.check_user_role import check_bd_user_role
from bd_handlers.get_post.get_post import get_posts


#Хендлер реагирует на комманду старт.
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = int(message.from_user.id)
    check_user_role = await check_bd_user_role(user_id=user_id)
    #Если роль пользователя админ то
    if check_user_role == 'admin':
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=admin_panel_keyboard_main_menu)
    #Если роль пользователя контент менеджер то
    elif check_user_role == 'cm':
        #Отправляем сообщение с клавиатурой
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Ваш ID: {message.from_user.id}",
                               reply_markup=cm_keyboard_main_menu)
    #Если нет роли пользователя то
    else:
        #SQL запрос
        rows = await get_posts()
        #Создаем лист с постами
        posts = []
        #Получаем пост из SQL запроса и добавляем его в лист posts
        for x in rows:
            post = x
            post_id = post['id']
            post_name = post['post_name']
            get_post = f'ID записи: {post_id}\nНазвание записи: {post_name}'
            posts.append(get_post)
        #Количество постов
        num_posts = (len(posts))
        #Если нет постов
        if num_posts == 0:
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Нет постов\n")
        #Если кол-во постов 1 то
        elif num_posts == 1:
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Записи BU11ZY:\n"
                               f"\n{posts[0]}\n")
        #Если кол-во постов 2 то
        elif num_posts == 2:
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Записи BU11ZY:\n"
                               f"\n{posts[0]}\n"
                               f"\n{posts[1]}\n")
        #Если кол-во постов 3 то
        elif num_posts == 3:
            await bot.send_message(chat_id=message.from_user.id,
                               text=f"Записи BU11ZY:\n"
                               f"\n{posts[0]}\n"
                               f"\n{posts[1]}\n"
                               f"\n{posts[2]}\n")