import os
import time
import signal
import requests
import subprocess


def begin_process():
    bash_command = """bash geocoords.sh"""
    return subprocess.Popen(bash_command,
                            stdout=subprocess.PIPE,
                            shell=True,
                            preexec_fn=os.setsid)


def end_process(process):
    return os.killpg(os.getpgid(process.pid), signal.SIGTERM)


def send_file(file_path, url):
    contents = open(file_path, 'r').read()
    r = requests.post(url=url,
                      data={
                          'device': 'AndroidPhone',
                          'user': 'rhdzmota'
                      },
                      files={
                          'file': (os.path.basename(file_path), contents)
                      })
    print(r.text)


def main():
    process = begin_process()
    time.sleep(10)
    end_process(process)


if __name__ == '__main__':
    main()
