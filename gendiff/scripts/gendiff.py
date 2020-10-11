# !/usr/bin/env python3  # noqa: C101

# -*- coding:utf-8 -*-

"""The main parsing script."""



from gendiff import cli
from gendiff.diif import generate_diff


def main():
    """Run a code."""
    old, new, format = cli.parse()
    generate_diff(old, new, format)


if __name__ == '__main__':
    main()
