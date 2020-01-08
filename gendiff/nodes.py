# -*- coding:utf-8 -*-

"""The module describes the rules for building nodes."""


def create_ast(before_file, after_file):
    """Build an abstract syntax tree.

    Arguments:
        before_file: first file to compare.
        after_file: second file to compare.

    Returns:
        dict.
    """
    common_keys = list(before_file.keys() | after_file.keys())
    return {key: get_node(before_file, after_file, key) for key in common_keys}


def get_node(before_file, after_file, key):  # noqa: WPS231
    """Return node.

    Args:
        before_file: First file for compare.
        after_file:  Second file for compare.
        key: Keyword for comparison.

    Returns:
        dict.
    """
    before = before_file.setdefault(key, None)
    after = after_file.setdefault(key, None)

    if before is None:  # noqa: WPS223
        return {
            'type': 'ADDED',
            'key': key,
            'value': after,
        }
    elif after is None:
        return {
            'type': 'DELETED',
            'key': key,
            'value': before,
        }
    elif isinstance(before, dict) and isinstance(after, dict):
        return {
            'type': 'PARRENT',
            'key': key,
            'child': create_ast(before, after),
        }
    elif before == after:
        return {
            'type': 'UNCHANGEABLE',
            'key': key,
            'value': after,
        }
    elif before != after:
        return {
            'type': 'CHANGEABLE',
            'key': key,
            'before_value': before,
            'after_value': after,
        }
