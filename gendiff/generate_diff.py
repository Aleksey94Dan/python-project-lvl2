import json
import os
import os.path


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


def get_diff_values(files, keys):
    # set_before = {get_first_file(files).get(key, None) for key in keys}
    # set_after = {get_second_file(files).get(key, None) for key in keys}
    return {
        key: {
            get_first_file(files).get(key, None),
            get_second_file(files).get(key, None),
            }
        for key in keys
    }



files = make_files(
    json.load(open('gendiff/after.json')),
    json.load(open('gendiff/before.json'))
    )
keys = get_common_keys(files)


print(os.getcwd())

# print(get_common_values(files, keys))
print(keys)
print()


file1 = 'after.json'
file2 = 'before.json'

file1_path = os.path.join(os.environ.get('HOME'), file1)
file2_path = os.path.join(os.environ.get('HOME'), file2)

print(file1_path)
print(file2_path)