import time
import numpy as np

from conf.settings import DataFilesConf, UserConf
from util.file_operations import get_file_contents, delete_file, create_file, send_file
from util.bash_process import start_process, end_process, reset_process
from util.datapoints_processing import extract_info, reset_needed


def one_iteration(process):

    # Read raw contents from csv
    recorded_datapoints = get_file_contents(DataFilesConf.FileNames.geo_data)
    if ',' not in recorded_datapoints:
        return process

    # Transform to datapoints list
    datapoints = list(filter(lambda x: '' not in x.split(','), recorded_datapoints.split('\n')))
    if reset_needed():
        process = reset_process(process)
        time.sleep(15)
        return process
    if len(datapoints) < 25:
        return process

    # Extract relevant info.
    datapoints_dicts, dates, coord_pairs, delta_time, delta_distance, speed = extract_info(datapoints)
    if len(speed) < 11:
        return process

    # Determine if trip has ended.
    if np.nanmean(speed[-10:]) < 3.5:
        if np.percentile(speed, 90) > 15:
            print('File send!')
            file_created = create_file(recorded_datapoints, date=dates[0].strftime('%Y%m%d'))
            r = send_file(file_path=file_created)
            print('Response: {}'.format(r.text))
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
    if not UserConf.user_name:
        raise Exception('User is not defined: see README.md for more details.')
    main()
