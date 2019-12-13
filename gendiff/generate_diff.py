# -*- coding:utf-8 -*-

"""Interface for calculating the difference of two files."""


import json
import os


def get_files(path_to_file):
    """
    Return from get_files the absolute path of the file.

    Args:
        path_to_file: The namepath to file.

    Returns:
        string.
    """
    worked_files = [os.path.split(path_to_file)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for document in files:
            if document in worked_files:
                path_to_file = os.path.join(root, document)
    return path_to_file


def make_files(path_to_first_file, path_to_second_file):
    """
    Return a pair of paths.

    Args:
        path_to_first_file: Absolute path to the first file.
        path_to_second_file: Absolute path to the second file.

    Returns:
        dictionary.
    """
    return {
        'after_file': json.load(open(path_to_first_file)),
        'before_file': json.load(open(path_to_second_file)),
    }


def get_first_file(files):
    """
    Return first file from files.

    Args:
        files: a pair from make_files.

    Returns:
        json.
    """
    return files['before_file']


def get_second_file(files):
    """
    Return second file from files.

    Args:
        files: a pair from make_files.

    Returns:
        json.
    """
    return files['after_file']


def get_common_keys(files):
    """
    Return a combined list of keys from two files.

    Args:
        files: a pair from make_files.

    Returns:
        list.
    """
    common_file = get_first_file(files).copy()
    common_file.update(get_second_file(files))
    return list(common_file.keys())


def get_deleted_data(files, keys):
    """
    Return deleted data.

    Args:
        files: a pair from make_files.
        keys: combined list of keys from two files.

    Returns:
        dictionary.
    """
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
    """
    Return added data.

    Args:
        files: a pair from make_files.
        keys: combined list of keys from two files.

    Returns:
        dictionary.
    """
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
    """
    Return unchanged data.

    Args:
        files: a pair from make_files.
        keys: combined list of keys from two files.

    Returns:
        dictionary.
    """
    return {
        key:
            list({get_second_file(files).get(key)}.intersection(
                {
                    get_first_file(files).get(key),
                }),
            )
            for key in keys
    }


def get_diff_data(files, kyes):
    """
    Return the difference of two files.

    Args:
        files: a pair from make_files.
        kyes: combined list of keys from two files.

    Returns:
        dictionary.
    """
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
    """
    Convert documet to json.

    Args:
        document: documet to convert.

    Returns:
        json.
    """
    return json.dumps(document, indent=2, separators=('', ': '))


def generate_diff(path_to_first_file, path_to_second_file):
    """
    Generate file differences into standart output stream.

    Args:
        path_to_first_file: Absolute path to the first file.
        path_to_second_file: Absolute path to the second file.

    Returns:
        json.
    """
    first_path = get_files(path_to_first_file)
    second_path = get_files(path_to_second_file)
    files = make_files(first_path, second_path)
    keys = get_common_keys(files)
    return convert_to_json(get_diff_data(files, keys)).replace('\"', '')
