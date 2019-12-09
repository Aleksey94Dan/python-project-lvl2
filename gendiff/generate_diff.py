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


def get_deleted_data(files, keys):
    d =  {
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

<<<<<<< HEAD
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
=======

def convert_to_json(data):
    return json.dumps(data, indent=4)

>>>>>>> 75468be29fda38bb7bc598592f9d49a7caedcf90