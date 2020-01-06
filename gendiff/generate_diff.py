# -*- coding:utf-8 -*-

"""Interface for calculating the difference of two files."""


import json
import os
import sys
import yaml


def get_files(path_to_file):
    worked_files = [os.path.split(path_to_file)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for document in files:
            if document in worked_files:
                path_to_file = os.path.join(root, document)
    extension = path_to_file.split('.')[-1]
    return path_to_file, extension


def make_files(path_to_first_file, path_to_second_file):
    first_file, extension_first_file = get_files(path_to_first_file)
    second_file, extension_second_file = get_files(path_to_second_file)
    if extension_first_file == 'json' and extension_second_file == 'json':
        return {
            'after_file': json.load(open(path_to_first_file)),
            'before_file': json.load(open(path_to_second_file)),
        }
    elif extension_first_file == 'yaml' and extension_second_file == 'yaml':
        return{
            'after_file': yaml.load(open(path_to_first_file), Loader=yaml.FullLoader),
            'before_file': yaml.load(open(path_to_second_file), Loader=yaml.FullLoader),
        }


def get_first_file(files):
    return files['before_file']


def get_second_file(files):
    return files['after_file']


def get_common_keys(files):
    common_file = get_first_file(files).copy()
    common_file.update(get_second_file(files))
    return list(common_file.keys())


def get_deleted_data(files, keys):
    return {
        key:
            list({get_first_file(files).get(key)}.difference(
                {
                    get_second_file(files).get(key),
                }),
            )
            for key in keys
    }


def get_added_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.difference(
                {
                    get_first_file(files).get(key),
                }),
            )
            for key in keys
    }


def get_unchangeable_data(files, keys):
    return {
        key:
            list({get_second_file(files).get(key)}.intersection(
                {
                    get_first_file(files).get(key),
                }),
            )
            for key in keys
    }


def get_diff_data(files, kyes):  # noqa: WPS210
    unchangeable_data = get_unchangeable_data(files, kyes)
    deleted_data = get_deleted_data(files, kyes)
    added_data = get_added_data(files, kyes)
    space, add, sub = ('  ', '+ ', '- ')
    diff_data = {}
    for key in kyes:
        if not deleted_data[key]:
            diff_data[space + key] = unchangeable_data[key][0]
        if deleted_data[key]:
            diff_data[add + key] = added_data[key][0]
            diff_data[sub + key] = deleted_data[key][0]
    return {
        key_of_diff: value_of_diff
        for key_of_diff, value_of_diff in diff_data.items()
        if value_of_diff
    }


def convert_to_json(document):
    return json.dumps(document, indent=2, separators=('', ': '))


def generate_diff(path_to_first_file, path_to_second_file):
    files = make_files(path_to_first_file, path_to_second_file)
    keys = get_common_keys(files)
    sys.stdout.write(convert_to_json(get_diff_data(files, keys)).replace('\"', ''))
    sys.stdout.write('\n')
    return convert_to_json(get_diff_data(files, keys)).replace('\"', '')



def main():
    files = make_files('/home/aleksey/HEXLET_ROOT/python-project-lvl2/gendiff/for_experiment/after1.json', '/home/aleksey/HEXLET_ROOT/python-project-lvl2/gendiff/for_experiment/after1.json')
    keys = get_common_keys(files)
    get_diff_data(files, keys)
    print(keys)


if __name__ == "__main__":
    main()