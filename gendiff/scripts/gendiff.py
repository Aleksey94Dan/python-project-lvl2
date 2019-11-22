#!/usr/bin/env python3

import argparse


def parse():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Generate diff',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')
    parser.parse_args()
    # parser.print_help()

def main():
    parse()


if __name__ == '__main__':
    main()
