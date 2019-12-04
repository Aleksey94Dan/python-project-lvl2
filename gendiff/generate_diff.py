import json


def make_files(file1, file2):
    return {
        'after_file': file1,
        'before_file': file2,
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
    return {
        key:
            {get_first_file(files).get(key)}.difference({get_second_file(files).get(key)})
            for key in keys
    }


def get_added_data(files, keys):
    return {
        key:
            {get_second_file(files).get(key)}.difference({get_first_file(files).get(key)})
            for key in keys
    }


def get_diff_data(files, kyes):
    first_file = get_first_file(files)
    second_file = get_second_file(files)
    deleted_data = get_deleted_data(files, kyes)
    added_data = get_added_data(files, keys)
    space, add, sub = ('   ', ' + ', ' - ')
    diff_data = dict()
    for key in keys:
        if len(deleted_data[key]) == 0:
            diff_data[space + key] = first_file[key]
        else:
            diff_data[add + key] = list(added_data[key])
            if None in diff_data[add + key]:
                del diff_data[add + key]
            diff_data[sub + key] = list(deleted_data[key])
            if None in diff_data[sub + key]:
                del diff_data[sub + key]
    return  diff_data




# print(get_common_values(files, keys))
print(keys)
print()
print(get_diff_values(files, keys))
