#Импорты
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

#Получение токена
config = dotenv_values(".env")
API_TOKEN = config['API_TOKEN']

#Настройка логгов
logging.basicConfig(level=logging.INFO)

#Запуск бота и диспатчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Первый хендлер, реагирует на старт и пересылает ваше сообщение, вам в чат + добавляет свое.
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ EchoBot!")

#Второй хендлер, реагирует на любой текст и присылает вам ваше сообщение.
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)