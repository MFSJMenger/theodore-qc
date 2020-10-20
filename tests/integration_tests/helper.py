import os


def get_folder_name(filename):
    return os.path.abspath(os.path.dirname(filename))


def file_diff(file1, file2, *, folder=None):
    if folder is not None:
        file1 = os.path.join(folder, file1)
        file2 = os.path.join(folder, file2)
    with open(file1, 'r') as f1:
        file1_txt = f1.read()
    with open(file2, 'r') as f2:
        file2_txt = f2.read()
    return file1_txt == file2_txt


def remove_file(filename, *, folder=None):
    if folder is not None:
        filename = os.path.join(folder, filename)
    if os.path.exists(filename):
        os.remove(filename)
