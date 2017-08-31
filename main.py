import os
import signal
import datetime
import subprocess
import numpy as np
from util.math import harversine
from conf.settings import DataFilesConf
from util.file_operations import get_file_contents, delete_file, create_file, send_file


def start_process():
    bash_command = """bash geocoords.sh"""
    return subprocess.Popen(bash_command,
                            stdout=subprocess.PIPE,
                            shell=True,
                            preexec_fn=os.setsid)


def end_process(process):
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    except:
        print("Couldn't end process.")


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


def one_iteration(process):
    recorded_datapoints = get_file_contents(DataFilesConf.FileNames.geo_data)
    if ',' not in recorded_datapoints:
        return process
    datapoints = list(filter(lambda x: '' not in x.split(','), recorded_datapoints.split('\n')))
    if len(datapoints) < 25:
        return process
    datapoints_dicts = list(map(lambda x: row_to_dict(x), datapoints))
    dates = list(map(lambda x: x['date'], datapoints_dicts))
    coord_pairs = list(map(lambda x: (x['lat'], x['lng']), datapoints_dicts))
    delta_time = list(map(lambda z: z.total_seconds() / 60 ** 2, paired_elems_apply(dates, lambda x, y: x - y)))
    delta_distance = paired_elems_apply(coord_pairs, harversine)
    speed = [d / t for d, t in zip(delta_distance, delta_time) if t > 0.1/60]
    if len(speed) < 11:
        return process
    if np.nanmean(speed[-10:]) < 3.5:
        if np.percentile(speed, 90) > 15:
            print('File saved!')
            file_created = create_file(recorded_datapoints, date=dates[0].strftime('%Y%m%d'))
            r = send_file(file_path=file_created, url='https://general-test-176923.appspot.com/trip')
        print("File deleted.")
        delete_file(DataFilesConf.FileNames.geo_data)
        end_process(process)
        process = start_process()
    return process


def procedure(process):
    while True:
        try:
            process = one_iteration(process)
        except:
            print("Something happened. Ending process...")
            end_process(process)
            print("Done.")
            break


def main():
    process = start_process()
    procedure(process)

if __name__ == '__main__':
    main()
