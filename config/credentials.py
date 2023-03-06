import dotenv
import os

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_CHARSET = os.environ.get('DB_CHARSET')
DB_COLLATION = os.environ.get('DB_COLLATION')
DB_DRIVER = os.environ.get('DB_DRIVER')
DB_URL = os.environ.get('DB_URL')