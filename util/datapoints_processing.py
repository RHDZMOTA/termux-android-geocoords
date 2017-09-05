import os
import datetime

from conf.settings import DataFilesConf
from util.math import harversine


def row_to_dict(row):
    elements = row.split(',')
    return {
        'date': datetime.datetime.strptime(elements[0] + ' ' + elements[1], '%d-%m-%Y %H:%M:%S'),
        'lat': float(elements[3]),
        'lng': float(elements[2]),
        'alt': float(elements[4]),
        'gps_speed': float(elements[5])}


def paired_elems_apply(vector, diff_function):
    return [diff_function(i, j) for i, j in zip(vector[1:], vector[:-1])]


def extract_info(datapoints):
    datapoints_dicts = list(map(lambda x: row_to_dict(x), datapoints))
    dates = list(map(lambda x: x['date'], datapoints_dicts))
    coord_pairs = list(map(lambda x: (x['lat'], x['lng']), datapoints_dicts))
    delta_time = list(map(lambda z: z.total_seconds() / 60 ** 2, paired_elems_apply(dates, lambda x, y: x - y)))
    delta_distance = paired_elems_apply(coord_pairs, harversine)
    speed = [d / t for d, t in zip(delta_distance, delta_time) if t > 0.1/60]
    return datapoints_dicts, dates, coord_pairs, delta_time, delta_distance, speed


def reset_needed():
    def get_last_row(rows, i=1):
        return rows[-i] if len(rows[-i]) else get_last_row(rows, i=i+1)

    now = datetime.datetime.now()
    if not os.path.exists(DataFilesConf.FileNames.geo_data):
        return True
    with open(DataFilesConf.FileNames.geo_data, 'r') as file:
        contents = file.read()
    if not len(contents):
        return False
    content_rows = contents.split('\n')
    try:
        last_row = get_last_row(content_rows)
        last_time = ' '.join(last_row.split(',')[:2])
        then = datetime.datetime.strptime(last_time, '%d-%m-%Y %H:%M:%S')
    except Exception as e:
        print(str(e))
        return False
    return True if (now - then).total_seconds() > 60 else False
