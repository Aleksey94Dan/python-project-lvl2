# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""Interface for calculating the difference of two files."""
import json
from gendiff.cli import make_files, get_after_data, get_before_data
from gendiff.nodes import generate_ast
from gendiff.reader import get_data_from_file


def visit(tree, key):
    if tree[key]["Identifier"] == "ADDED":
        return {'+ ' + key: tree[key]["Value"]}
    elif tree[key]["Identifier"] == "DELETED":
        return {'- ' + key: tree[key]["Value"]}
    elif tree[key]["Identifier"] == "CHANGEABLE":
        return {'+ ' + key: tree[key]["After_value"],
                '- ' + key: tree[key]["Before_value"],
        }
    elif tree[key]["Identifier"] == "UNCHANGEABLE":
        return {'  ' + key: tree[key]["Value"]}
    elif tree[key]["Identifier"] == "PARENT":
        return {key: render(tree[key]["Child"])}


def render(data):
    keys = list(data.keys())
    a = {}
    for key in keys:
        a.update(visit(data, key))
    return a


def generate_diff(path_to_first_file, path_to_second_file):
    before_file = get_data_from_file(path_to_first_file)
    after_file = get_data_from_file(path_to_second_file)
    files = make_files(before_file, after_file)
    before = get_before_data(files)
    after = get_after_data(files)
    ast = render(generate_ast(before, after))
    diff = json.dumps(ast, indent=2).replace("\"",'').replace(",",'')
    return diff


def main():
    print(generate_diff('gendiff/tests/fixtures/before.json','gendiff/tests/fixtures/after.json'))

    path_to_first_file = 'gendiff/tests/fixtures/before_inserted.json'
    path_to_second_file = 'gendiff/tests/fixtures/after_inserted.json'
    print()
    print(generate_diff(path_to_first_file, path_to_second_file))


if __name__ == "__main__":
    main()