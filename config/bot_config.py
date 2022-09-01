#Импорты
import logging
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage


#Получение токена из файла .env
config = dotenv_values('./config/.env')
API_TOKEN = config['API_TOKEN']
ADMIN = int(config['ADMIN'])

#Настройка логгов
logging.basicConfig(level=logging.INFO)

#Запуск бота и диспатчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())