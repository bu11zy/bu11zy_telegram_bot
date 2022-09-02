#Импорты
import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values

#Файл с конфигами
config = dotenv_values(CONFIG_DIR / '.env')


#Конфиги
USER = config['user']
PSWD = config['password']
DB = config['database']
HOST = config['host']


#Sql функция
async def check_bd_user_name(user_id):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    row = await conn.fetchrow('SELECT user_name FROM user_role WHERE user_id = $1', user_id,)
    await conn.close()
    if row is None:
        return 'None'
    else:
        return row['user_name']