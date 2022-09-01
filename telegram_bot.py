#Импорты
from aiogram import executor
from config.bot_config import dp
from handlers.admin_panel.create_post import *
from handlers.admin_panel.delete_post import *
from handlers.admin_panel.main_menu import *
from handlers.start.start import *
from handlers.admin_panel.cancel import *
from handlers.admin_panel.create_user_role.create_user_role import *
from handlers.admin_panel.create_user_role.admin.admin import *
from handlers.admin_panel.create_user_role.cm.cm import *
#from handlers.test.test import *




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
