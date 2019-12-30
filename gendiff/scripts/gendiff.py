# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""The main parsing script."""


from gendiff.generate_diff import generate_diff
from gendiff.parsers.gendiff import parse


def main():
    generate_diff(*parse())


if __name__ == "__main__":
    main()
