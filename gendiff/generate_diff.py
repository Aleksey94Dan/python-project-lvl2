# -*- coding:utf-8 -*-
# !/usr/bin/env python3
import pprint
import json

"""Interface for calculating the difference of two files."""

from cli import make_files, get_after_data, get_before_data
from nodes import create_ast

def formatter(ast, key):
    if ast[key]['type'] is 'ADDED':
        return {'+ {}'.format(key): ast[key]['value']}
    elif ast[key]['type'] is 'DELETED':
        return {'- {}'.format(key): ast[key]['value']}
    elif ast[key]['type'] is 'UNCHANGEABLE':
        return {key: ast[key]['value']}
    elif ast[key]['type'] is 'CHANGEABLE':
        return {key: {"-":ast[key]['before_value'], "+":ast[key]['after_value']}}
    elif ast[key]['type'] is 'PARRENT':
        return gene_visit(ast[key]['child'])

def gene_visit(ast):
    keys = sorted(list(ast.keys()))
    return {key: formatter(ast, key) for key in keys}





if __name__ == "__main__":
    files = make_files('gendiff/tests/fixtures/after1.json',
    'gendiff/tests/fixtures/before1.json')
    before = get_before_data(files)
    after = get_after_data(files)
    ast = create_ast(before, after)
    # print(files)
    # print()
    # print(before)
    # print()
    # print(after)
    # print()
    # print(json.dumps(ast, indent=4))
    # print()
    # print(json.dumps(ast, indent=4))
    print()
    # keys = sorted(list(ast.keys()))
    # print(keys)
    # # d = {}
    # if ast['group3']['type'] is "ADDED":
    #     d[' + group3'] = ast['group3']["value"]
    # if ast['group2']['type'] is "DELETED":
    #     d[' - group2'] = ast['group2']["value"]
    # print(gene_visit(ast))
    # print(formatter(ast, 'group1'))
    # print(formatter(ast, 'group2'))
    # print(formatter(ast, 'group3'))
    # print(formatter(ast, 'common'))
    print(json.dumps(gene_visit(ast), indent=4))
    # print(ast['group1']['child'])


