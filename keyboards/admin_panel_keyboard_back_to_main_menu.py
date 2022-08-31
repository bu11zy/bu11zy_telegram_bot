#Импорты
from aiogram import types


#Клавиатура "Админ Панель вернуться в главное меню"
admin_panel_keyboard_back_to_main_menu = types.InlineKeyboardMarkup()
#Кнопка admin_panel_btn_main_menu
ap_btn_mm = types.InlineKeyboardButton('Вернуться в главное меню',
                                       callback_data='main_menu')
#Добавляем кнопки в клавиатуру
admin_panel_keyboard_back_to_main_menu.row(ap_btn_mm)