from conf.settings import DataFilesConf
import subprocess
import os


def create_dir_if_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def install_termux_dependencies():
    bash_command = """bash termux_dependencies.sh"""
    subprocess.check_output(['bash', '-c', bash_command])


if __name__ == '__main__':
    print(DataFilesConf.Paths.data)
    create_dir_if_exists(DataFilesConf.Paths.data)
    install_termux_dependencies()
