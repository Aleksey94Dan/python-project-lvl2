# !/usr/bin/env python3  # noqa: C101

# -*- coding:utf-8 -*-

"""The main parsing script."""


from gendiff import cli
from gendiff.diff import generate_diff


def main():
    """Run a code."""
    old, new, formater = cli.parse()
    print(generate_diff(old, new, formater))  # noqa: T001


if __name__ == '__main__':
    main()
