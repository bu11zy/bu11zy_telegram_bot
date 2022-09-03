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
async def change_post(post_name, post_disc, post_tag, post_link, change_user_name, change_date, change_time, post_id):
    conn = await asyncpg.connect(user=USER, password=PSWD, database=DB, host=HOST)
    await conn.execute('UPDATE posts SET post_name=$1, post_disc=$2, post_tag=$3, post_link=$4, change_user_name=$5, change_date=$6, change_time=$7'
                       'WHERE id=$8', 
                       post_name, post_disc, post_tag, post_link, change_user_name, change_date, change_time, post_id,)
    await conn.close()
