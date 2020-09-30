# !/usr/bin/env python3  # noqa: C101

# -*- coding:utf-8 -*-

"""The main parsing script."""


import sys

from gendiff import parsers


def main():
    """Run a code."""
    sys.stdout.write(parsers.parse())


if __name__ == '__main__':
    main()
