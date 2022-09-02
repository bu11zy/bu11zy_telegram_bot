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
async def get_post_name(post_id):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    row = await conn.fetchrow('SELECT post_name FROM posts WHERE id=$1', post_id)
    await conn.close()
    if row is None:
        return 'None'
    else:
        return row