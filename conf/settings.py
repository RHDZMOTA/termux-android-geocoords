from os import environ, pardir
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DATA_DIR_NAME = environ.get('DATA_DIR_NAME')
GEO_DATA_FILENAME = environ.get('GEO_DATA_FILENAME')
DETECTED_TRIP_FILENAME = environ.get('DETECTED_TRIP_FILENAME')
USER_NAME = environ.get('USER_NAME')
USER_EMAIL = environ.get('USER_EMAIL')
TERMUX_GEOCOORD_API = environ.get('TERMUX_GEOCOORD_API')

PROJECT_DIR = abspath(join(dirname(__file__), pardir))
DATA_PATH = join(PROJECT_DIR, DATA_DIR_NAME)


class DataFilesConf:
    class Paths:
        data = DATA_PATH

    class FileNames:
        detected_trip = join(DATA_PATH, DETECTED_TRIP_FILENAME)
        geo_data = join(DATA_PATH, GEO_DATA_FILENAME)


class UserConf:
    user_name = USER_NAME if len(USER_NAME) else None
    user_email = USER_EMAIL if len(USER_EMAIL) else None