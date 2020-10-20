from subprocess import run
import os
from . import get_folder_name
from contextlib import contextmanager


PWD = get_folder_name(__file__)
THEOBIN = os.path.join(PWD, "../../bin/")

ANALYZE_TDEN = os.path.join(THEOBIN, "analyze_tden.py")

@contextmanager
def exec_in_folder(folder):
    path = os.getcwd()
    if folder is not None:
        os.chdir(folder)
        yield
    os.chdir(path)


def execute(command, *, folder=None):
    with exec_in_folder(folder):
        return run([command], shell=True)


def call_tden(filename, *, folder=None):
    execute(f"{ANALYZE_TDEN} -f {filename}", folder=folder)
