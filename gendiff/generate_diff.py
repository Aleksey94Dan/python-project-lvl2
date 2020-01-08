# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""Interface for calculating the difference of two files."""

from cli import make_files, get_after_data, get_before_data
from nodes import create_ast

if __name__ == "__main__":
    files = make_files('gendiff/tests/fixtures/after1.json',
    'gendiff/tests/fixtures/before1.json')
    before = get_before_data(files)
    after = get_after_data(files)
    ast = create_ast(before, after)
    print(files)
    print()
    print(before)
    print()
    print(after)
    print()
    print(ast)