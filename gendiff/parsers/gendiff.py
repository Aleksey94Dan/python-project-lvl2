# -*- coding:utf-8 -*-


import argparse


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
    return path1, path2
