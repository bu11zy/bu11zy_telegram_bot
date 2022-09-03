from keyboards.admin_panel_keyboard_back_to_main_menu import admin_panel_keyboard_back_to_main_menu
from aiogram import types
from config.bot_config import dp, bot
from aiogram.dispatcher import FSMContext
from handlers.admin_panel.delete_post.delete_post import FSM_delete_post
from bd_handlers.change_post.get_post_name import get_post_name
from bd_handlers.delete_post.delete_post import delete_post


#В этой функции удаляется пост
@dp.message_handler(state=FSM_delete_post.post_id)
async def post_id(message: types.Message, state: FSMContext):
    #Проверяем исключения
    async with state.proxy() as data:
        try:
            #SQL функция, если row=None, то ошибка TypeError
            row = await get_post_name(int(message.text))
            data['post_id'] = str(message.text)
            post_id = int(data['post_id'])
            #Переходим к следующему состоянию
            await delete_post(post_id=post_id)
            await state.finish()
            #Отправляем сообщение
            await bot.send_message(chat_id=message.from_user.id,
                                   text=f"ID записи: {post_id}\n"
                                   f"Имя записи: {row['post_name']}\n"
                                   f"Удалена\n",
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