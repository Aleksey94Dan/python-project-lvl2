from gendiff import format
from gendiff.files import load
import argparse


def formatter(name):
    """Return the formatting function according to the specified format."""
    if name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    elif name == format.JSON:
        return format.json
    raise argparse.ArgumentTypeError(
        'Unknown formatter: "{0}". Use one of this: {1}'.format(
            name,
            ', '.join(format.FORMATTERS),
        ),
    )


def parse():
    """Parser command line arguments."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('old', type=load)
    parser.add_argument('new', type=load)
    parser.add_argument(
        '-f',
        '--format',
        default=format.DEFAULT,
        type=formatter,
        help='set format of output',
    )
    args = parser.parse_args()
    return (
        args.old,
        args.new,
        args.format,
    )
