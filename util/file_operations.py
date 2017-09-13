from conf.settings import DataFilesConf, UserConf, TERMUX_GEOCOORD_API
import requests
import time
import os


def delete_file(file_path):
    os.remove(file_path)


def get_file_contents(file_path):
    try:
        with open(file_path) as file:
            file_contents = file.read()
    except Exception as e:
        # print(str(e))
        file_contents = ''
    return file_contents


def replace_string(target, elements, value):
    return target if not len(elements) else replace_string(target.replace(elements[0], value), elements[1:], value)


def generate_trip_filename(date):
    files = list(filter(lambda x: date in x, os.listdir(DataFilesConf.Paths.data)))
    if not len(files):
        return DataFilesConf.FileNames.detected_trip.format(date=date, id=1, user=UserConf.user_name)
    last_id = max(list(map(lambda x: int(replace_string(x, [date, "trip.csv", "_", UserConf.user_name], '')), files)))
    return DataFilesConf.FileNames.detected_trip.format(date=date, id=last_id+1, user=UserConf.user_name)


def create_file(file_contents, date):
    file_path = generate_trip_filename(date)
    with open(file_path, 'w') as file:
        file.write(file_contents)
    return file_path


def send_file(file_path, limit_try=10):
    params = {
        'content-type': 'multipart/form-data',
        'user': UserConf.user_name,
        'pwd': 'crabi-is-great',
        'filename': os.path.basename(file_path)}
    file_payload = {
        'file': open(file_path, 'rb')
    }
    try:
        r = requests.post(url=TERMUX_GEOCOORD_API, data=params, files=file_payload)
        print(r.text)
    except Exception as e:
        print(str(e))
        time.sleep(3)
        r = None
    return send_file(file_path, limit_try-1) if ((limit_try > 0) and (r is None)) else r
