import os
from typing import Final

import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

DB_HOST: Final = os.environ.get('DB_HOST')
DB_PORT: Final = os.environ.get('DB_PORT')
DB_USER: Final = os.environ.get('DB_USER')
DB_PASSWORD: Final = os.environ.get('DB_PASSWORD')
DB_NAME: Final = os.environ.get('DB_NAME')
DB_CHARSET: Final = os.environ.get('DB_CHARSET')
DB_COLLATION: Final = os.environ.get('DB_COLLATION')
DB_DRIVER: Final = os.environ.get('DB_DRIVER')
DB_URL: Final = os.environ.get('DB_URL')
