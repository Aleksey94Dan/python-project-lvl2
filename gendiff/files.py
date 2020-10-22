# -*- coding:utf-8 -*-

"""Uploads YAML and Json files."""
import argparse
import json
import os

import yaml

_get_loader = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def load(path):
    """Get data on the specified path."""
    path_to_file = os.path.abspath(path)
    _, extension = os.path.splitext(path_to_file)
    loader = _get_loader(extension)
    if not loader:
        raise argparse.ArgumentTypeError(
            'Unsupported {0} extension'.format(extension),
        )
    try:
        with open(path_to_file) as file_name:
            return loader(file_name)
    except (json.JSONDecodeError, yaml.YAMLError):
        raise argparse.ArgumentTypeError(
            'Incorrect structure files. '  # noqa: WPS326
            'Become familiar with the JSON/YML compilation rules.',
        )
