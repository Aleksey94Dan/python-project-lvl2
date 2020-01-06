import json
import os


deleted = 'DELETED'
added = 'ADDED'
unchangeable = 'UNCHANGEABLE'

def get_path_to_files(path_to_file):
    worked_files = [os.path.split(path_to_file)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for document in files:
            if document in worked_files:
                path_to_file = os.path.join(root, document)
    # extension = path_to_file.split('.')[-1]
    return path_to_file


def get_data_from_file(abs_path_to_file):
    with open(abs_path_to_file) as f:
        data_from_file = json.load(f)
    return data_from_file


def get_common_keys(after_file, before_file):
    common_keys = list(after_file.keys() | before_file.keys())
    return common_keys


def AST_builder(after_file, before_file, key):
    after = after_file.setdefault(key, None)
    before = before_file.setdefault(key, None)

    if after  is None:
        node = {
            'type': 'deleted',
            'key': key,
            'value': before,
        }
    elif before is None:
        node = {
            'type': 'added',
            'key': key,
            'value': after,
        }
    elif  before == after:
        node = {
            'type': 'неизменяемый',
            'key': key,
            'value': before,
        }
    elif isinstance(after, dict) and isinstance(before, dict):
            node = {
            'type': 'неизменяемый',
            'key': key,
            'child': AST_builder(after, before, key)
        }
    elif before != after:
        node = {
            'type': 'измененный',
            'key': key,
            'old_value': before,
            'new_value': after,
        }
    return node




def main():
    path_to_after = get_path_to_files('gendiff/for_experiment/after1.json')
    path_to_before = get_path_to_files('gendiff/for_experiment/before1.json')
    after_file = get_data_from_file(path_to_after)
    before_file = get_data_from_file(path_to_before)

    {}
    keys = get_common_keys(after_file, before_file)
    for key in keys:
        print(AST_builder(after_file, before_file, key))



if __name__ == "__main__":
    main()
