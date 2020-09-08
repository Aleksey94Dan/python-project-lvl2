# -*- coding:utf-8 -*-

"""Parser for command-line options,arguments and extenstions."""

import argparse
import json
import os

import yaml

EXTENSIONS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def _get_data_from_file(path):
    path_to_file = os.path.abspath(path)
    extension = os.path.splitext(path_to_file)[-1]
    if not EXTENSIONS(extension):
        raise argparse.ArgumentTypeError(
            'Unsupported  {0} extension'.format(extension),
        )
    with open(path_to_file) as file_name:
        return EXTENSIONS(extension)(file_name)


def parse():
    """Parser command line arguments."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
        )
    parser.add_argument('first_file', type=_get_data_from_file)
    parser.add_argument('second_file', type=_get_data_from_file)
    parser.add_argument(
        '-f',
        '--format',
        # default=,  # noqa: T002
        # type=,
        help='set format of output',
    )
    parser.parse_args()
