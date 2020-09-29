# -*- coding:utf-8 -*-

"""Parser for command-line options,arguments and extenstions."""
import argparse
import json
import os
import sys

import yaml

from gendiff import format
from gendiff.diif import generate_diff

EXTENSIONS = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def formatter(name):
    """Return the formatting function according to the specified format."""
    if name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    elif name = format.JSON:
        return format.json
    raise argparse.ArgumentTypeError(
        'Unknown formatter: "{0}". Use one of this: {1}'.format(
            name,
            ', '.join(format.FORMATTERS),
        ),
    )


def get_data_from_file(path):
    """Get data on the specified path."""
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
    parser.add_argument('first_file', type=get_data_from_file)
    parser.add_argument('second_file', type=get_data_from_file)
    parser.add_argument(
        '-f',
        '--format',
        default=format.DEFAULT,
        type=formatter,
        help='set format of output',
    )
    args = parser.parse_args()
    sys.stdout.write(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
        ),
    )
