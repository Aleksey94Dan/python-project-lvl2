import json
import os


def get_files(file1):
    worked_files = [os.path.split(file1)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if file in worked_files:
                path_to_file = os.path.join(root, file)
    return path_to_file


def make_files(path_to_file1, path_to_file2):
    return {
        'after_file': json.load(open(path_to_file1)),
        'before_file': json.load(open(path_to_file2)),
    }


def get_first_file(file):
    return file['before_file']


def get_second_file(file):
    return file['after_file']


def get_common_keys(files):
    common_file = get_first_file(files).copy()
    common_file.update(get_second_file(files))
    return list(common_file.keys())


def get_deleted_data(files, keys):
    d = {
        key:
            list({get_first_file(files).get(key)}.difference(
                {get_second_file(files).get(key)}))
            for key in keys
    }
    return d


def get_added_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.difference(
                {get_first_file(files).get(key)}))
            for key in keys
    }


def get_unchangeable_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.intersection(
                {get_first_file(files).get(key)}))
            for key in keys
    }


def get_diff_data(files, kyes):
    unchangeable_data = get_unchangeable_data(files, kyes)
    deleted_data = get_deleted_data(files, kyes)
    added_data = get_added_data(files, kyes)
    space, add, sub = ('   ', ' + ', ' - ')
    diff_data = dict()
    for key in kyes:
        if len(deleted_data[key]) == 0:
            diff_data[space + key] = unchangeable_data[key][0]
        else:
            diff_data[add + key] = added_data[key][0]
            diff_data[sub + key] = deleted_data[key][0]
    return {key: value for key, value in diff_data.items() if value}


def convert_to_json(data):
    return json.dumps(data, indent=4)


def generate_diff(path_to_file1, path_to_file2):
    path1 = get_files(path_to_file1)
    path2 = get_files(path_to_file2)
    files = make_files(path1, path2)
    keys = get_common_keys(files)
    data = get_diff_data(files, keys)
    return convert_to_json(data)
