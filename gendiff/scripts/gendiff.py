# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""The main parsing script."""


import argparse
import sys

from gendiff.generate_diff import generate_diff


def parse():
    """Return interface command-line."""
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    path1 = args.first_file
    path2 = args.second_file
    sys.stdout.write(generate_diff(path1, path2))
    sys.stdout.write('\n')


def main():
    """Run a script."""
    parse()


if __name__ == '__main__':
    main()
