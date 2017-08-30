from os import environ, pardir
from os.path import join, dirname, abspath

DATA_DIR_NAME = 'data'
PROJECT_DIR = abspath(join(dirname(__file__), pardir))
DATA_PATH = join(PROJECT_DIR, DATA_DIR_NAME)

GEO_DATA_FILENAME = 'geo_data.csv'
LAST_DATAPOINTS_FILENAME = 'last_datapoints.csv'
DETECTED_TRIP_FILENAME = 'actual_trip.csv'


class DataFilesConf:
    class Paths:
        data = DATA_PATH

    class FileNames:
        last_datapoints = join(DATA_PATH, LAST_DATAPOINTS_FILENAME)
        detected_trip = join(DATA_PATH, DETECTED_TRIP_FILENAME)
        geo_data = join(DATA_PATH, GEO_DATA_FILENAME)
