import os
import shutil


def save_to_disk(content: str, path: str, file_name: str):
    make_folder(path)
    file = get_full_path_to_file_in_folder(file_name, path)
    save_file(content, file)


def get_full_path_to_folder(sub_path: str) -> str:
    abs_path = os.path.abspath(sub_path)
    if "job1" in abs_path:
        return abs_path.replace("job1", "storage")
    return abs_path.replace("job2", "storage")


def get_full_path_to_file_in_folder(file: str, sub_path: str) -> str:
    return os.path.join(get_full_path_to_folder(sub_path), file)


def make_folder(path: str):
    clean_root_folder(path)
    cwd = get_full_path_to_folder(path)
    os.makedirs(cwd)


def clean_root_folder(path: str):
    sub_path = get_full_path_to_folder(get_sub_path_root(path))
    if os.path.exists(sub_path):
        shutil.rmtree(sub_path)


def get_sub_path_root(path: str) -> str:
    path_separator = '\\'
    other_separator = '/'
    if other_separator in path:
        path_separator = other_separator
    return path.split(path_separator)[0]


def save_file(json_content: str, file: str):
    with open(file, 'w') as file:
        file.write(json_content)
        file.close()


def is_folder_empty(path: str) -> bool:
    sub_path = get_full_path_to_folder(path)
    if not list_folder(sub_path):
        return True
    if not os.listdir(sub_path):
        return True
    return False


def list_folder(path: str) -> list[str]:
    return os.listdir(get_full_path_to_folder(path))


def get_file_name(path: str) -> str:
    return os.path.splitext(path)[0]
