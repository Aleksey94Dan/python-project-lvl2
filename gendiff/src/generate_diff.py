import json
import os.path


def make_files(path_to_file1, path_to_file2):
    return {
        'after_file': json.load(open(os.path.abspath(path_to_file1))),
        'before_file': json.load(open(os.path.abspath(path_to_file2))),
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
            list({get_first_file(files).get(key)}.difference({get_second_file(files).get(key)}))
            for key in keys
    }
    return d


def get_added_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.difference({get_first_file(files).get(key)}))
            for key in keys
    }


def get_unchangeable_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.intersection({get_first_file(files).get(key)}))
            for key in keys
    }



def get_diff_data(files, kyes):
    unchangeable_data = get_unchangeable_data(files, keys)
    deleted_data = get_deleted_data(files, kyes)
    added_data = get_added_data(files, keys)
    space, add, sub = ('   ', ' + ', ' - ')
    diff_data = dict()
    for key in keys:
        if len(deleted_data[key]) == 0:
            diff_data[space + key] = unchangeable_data[key][0]
        else:
            diff_data[add + key] = added_data[key][0]
            diff_data[sub + key] = deleted_data[key][0]
    return {key: value for key, value in diff_data.items() if value}


def convert_to_json(data):
    return json.dumps(data, indent=4)


# path1 = '/home/all_done/Hexlet/projects/python-project-lvl2/gendiff/after.json'
# path2 = '/home/all_done/Hexlet/projects/python-project-lvl2/gendiff/before.json'

path1 = 'gendiff/after.json'
path2 = 'gendiff/before.json'

files = make_files(path1, path2)

keys = get_common_keys(files)
print(keys)
print(get_diff_data(files, keys))
data = get_diff_data(files, keys)
print(convert_to_json(data))