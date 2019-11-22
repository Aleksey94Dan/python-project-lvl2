#!/usr/bin/env python3

import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='%(prog)s [-h] [-f FORMAT] first_file second_file',
        description='Generate diff',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help=argparse.SUPPRESS)
    parser.parse_args()


def main():
    parse()


if __name__ == '__main__':
    main()
