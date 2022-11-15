import os
from dotenv import load_dotenv


load_dotenv()


class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = os.environ["MYSQL_HOST"]
    MYSQL_USER = os.environ["MYSQL_USER"]
    MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
    MYSQL_DB = os.environ["MYSQL_DB"]


serverConfig = {
    "development": DevelopmentConfig
}
