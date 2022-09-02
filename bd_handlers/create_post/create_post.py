import asyncpg
from config.bot_config import CONFIG_DIR
from dotenv import dotenv_values


#Файл с конфигами
config = dotenv_values(CONFIG_DIR / '.env')


#Конфиги
user = str(config['user'])
password = str(config['password'])
database = str(config['database'])
host = str(config['host'])


#Sql функция
async def create_post(post_name, post_disc, post_tag, post_link, user_name, create_data, create_time):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''INSERT INTO posts(post_name, post_disc, post_tag, post_link, user_name, create_data, create_time)
                       VALUES($1, $2, $3, $4, $5, $6, $7)''',
                       post_name, post_disc, post_tag, post_link, user_name, create_data, create_time)
    await conn.close()