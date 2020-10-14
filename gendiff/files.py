# -*- coding:utf-8 -*-

"""Uploads YAML and Json files."""
import argparse
import json
import os

import yaml


def _get_loader(extension):
    return {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(extension)


def load(path):
    """Get data on the specified path."""
    path_to_file = os.path.abspath(path)
    _, extension = os.path.splitext(path_to_file)
    error_message1 = 'Incorrect structure files.'
    error_message2 = 'Become familiar with the JSON/YAML compilation rules.'
    if not _get_loader(extension):
        raise argparse.ArgumentTypeError(
            'Unsupported {0} extension'.format(extension),
        )
    try:
        with open(path_to_file) as file_name:
            return _get_loader(extension)(file_name)
    except Exception:
        raise argparse.ArgumentTypeError(
            ' '.join((error_message1, error_message2)),
        )
