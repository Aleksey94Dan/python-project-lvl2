# -*- coding:utf-8 -*-

"""Interface for calculating the difference of two files."""


from gendiff.cli import get_after_data, get_before_data, make_files
from gendiff.nodes import generate_ast
from gendiff.reader import get_data_from_file


def visit(tree, key):
    if tree[key]['Identifier'] == 'ADDED':
        return {'+ ' + key: tree[key]['Value']}
    elif tree[key]['Identifier'] == 'DELETED':
        return {'- ' + key: tree[key]['Value']}
    elif tree[key]['Identifier'] == 'CHANGEABLE':
        return {
            '+ ' + key: tree[key]['After_value'],
            '- ' + key: tree[key]['Before_value'],
        }
    elif tree[key]['Identifier'] == 'UNCHANGEABLE':
        return {'  ' + key: tree[key]['Value']}
    elif tree[key]['Identifier'] == 'PARENT':
        return {'  ' + key: render(tree[key]['Child'])}


def render(node):
    keys = list(node.keys())
    updated_node = {}
    for key in keys:
        updated_node.update(visit(node, key))
    return updated_node


def generate_diff(path_to_first_file, path_to_second_file):
    before_file = get_data_from_file(path_to_first_file)
    after_file = get_data_from_file(path_to_second_file)
    files = make_files(before_file, after_file)
    before = get_before_data(files)
    after = get_after_data(files)
    diff = render(generate_ast(before, after))
    return diff
