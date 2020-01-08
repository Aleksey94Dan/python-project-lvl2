# -*- coding:utf-8 -*-

"""Reading data from files."""

import json
import os

import yaml

EXTENSION = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def get_path_to_files(path_to_file):  # noqa: WPS210
    """Get absolute file path.

    Args:
        path_to_file: The namepath to file.

    Returns:
        tuple(str, str).
    """
    worked_file = [os.path.split(path_to_file)[-1]]
    path_to_file = ''
    for root, _, files in os.walk(os.getcwd()):
        for document in files:
            if document in worked_file:
                path_to_file = os.path.join(root, document)
    extension = path_to_file.split('.')[-1]
    return path_to_file, extension


def get_data_from_file(path_to_file):
    """Return data from a file depending on the extension.

    Args:
        path_to_file: The namepath to file.

    Returns:
        dict.
    """
    data_file, extension_of_file = get_path_to_files(path_to_file)
    with open(data_file) as data_from_file:
        return EXTENSION[extension_of_file](data_from_file)
