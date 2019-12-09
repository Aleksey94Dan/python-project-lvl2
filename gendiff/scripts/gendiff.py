#!/usr/bin/env python3

import argparse
from .generate_diff import generate_diff


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    # parser.parse_args()
    args = parser.parse_args()
    path1 = args.first_file
    path2 = args.second_file
    print(generate_diff(path1, path2))


def main():
    parse()


if __name__ == '__main__':
    main()
