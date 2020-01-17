# -*- coding:utf-8 -*-
# !/usr/bin/env python3

"""Interface for calculating the difference of two files."""
import json
from cli import make_files, get_after_data, get_before_data
from nodes import create_ast


def formatter(tree, key):
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
        return {key: generate_visit(tree[key]["Child"])}


def generate_visit(data):
    keys = list(data.keys())
    a = {}
    for key in keys:
        a.update(formatter(data, key))
    return a



if __name__ == "__main__":
    files = make_files('gendiff/tests/fixtures/after1.json',
    'gendiff/tests/fixtures/before1.json')
    before = get_before_data(files)
    after = get_after_data(files)
    ast = create_ast(before, after)
    print()
    print(json.dumps(generate_visit(ast), indent=4))
    print()
    print()
    files = make_files('gendiff/tests/fixtures/after.json',
    'gendiff/tests/fixtures/before.json')
    before = get_before_data(files)
    after = get_after_data(files)
    ast = create_ast(before, after)
    print()
    print(json.dumps(generate_visit(ast), indent=4))