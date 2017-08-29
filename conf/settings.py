from os import environ, pardir
from os.path import join, dirname, abspath

DATA_DIR_NAME = 'data'
PROJECT_DIR = abspath(join(dirname(__file__), pardir))
DATA_PATH = join(PROJECT_DIR, DATA_DIR_NAME)


class DataFilesConf:
    class Paths:
        data = DATA_PATH
