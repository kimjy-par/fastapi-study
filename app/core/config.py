import os

from dotenv import load_dotenv

load_dotenv()

class Setting():
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

    DATABASE_URI='mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(
        user=MYSQL_USER, 
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DATABASE,        
    )

settings = Setting()
