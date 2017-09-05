import os
import signal
import subprocess


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
        print("Warning: Couldn't end process.")


def reset_process(process):
    end_process(process)
    return start_process()

