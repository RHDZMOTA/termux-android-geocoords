from conf.settings import DataFilesConf
import requests
import os


def delete_file(file_path):
    os.remove(file_path)


def get_file_contents(file_path):
    try:
        with open(file_path) as file:
            file_contents = file.read()
    except:
        file_contents = ''
    return file_contents


def generate_trip_filename(date):
    files = list(filter(lambda x: date in x, os.listdir(DataFilesConf.Paths.data)))
    if not len(files):
        return DataFilesConf.FileNames.detected_trip.format(date=date, id=1)
    last_id = max(list(map(lambda x: int(x.replace(date, "").replace("trip.csv", "").replace("_", "")),
                           files)))
    return DataFilesConf.FileNames.detected_trip.format(date=date, id=last_id+1)


def create_file(file_contents, date):
    file_path = generate_trip_filename(date)
    with open(file_path, 'w') as file:
        file.write(file_contents)


def send_file(file_contents, url, limit_try=10):
    data = {
        'device': 'AndroidPhone',
        'user': 'rhdzmota'}
    files = (DataFilesConf.FileNames.geo_data, file_contents)
    try:
        r = requests.post(url=url, data=data, files=files)
        print(r.text)
    except:
        r = None
    return send_file(file_contents, url, limit_try-1) if ((limit_try > 0) and (r is None)) else r