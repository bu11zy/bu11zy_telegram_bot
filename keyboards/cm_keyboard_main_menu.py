#Импорты
from aiogram import types


#Клавиатура "Контент менеджер главное меню"
cm_keyboard_main_menu = types.InlineKeyboardMarkup()
#Кнопка cm_keyboard_btn_create_post
ap_btn_cp = types.InlineKeyboardButton('Создать пост',
                                       callback_data='create_post')
#Кнопка cm_keyboard_btn_delete_post
ap_btn_dp = types.InlineKeyboardButton('Удалить пост',
                                       callback_data='delete_post')
#Кнопка cm_keyboard_btn_change_post
ap_btn_chp = types.InlineKeyboardButton('Изменить пост',
                                       callback_data='change_post')


#Клавиатура cm_keyboard_main_menu
cm_keyboard_main_menu.row(ap_btn_cp, ap_btn_dp)
cm_keyboard_main_menu.row(ap_btn_chp)