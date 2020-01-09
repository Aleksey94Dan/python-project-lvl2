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
    return {key: get_node(before_file, after_file, key) for key in sorted(common_keys)}


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
            'type': 'DELETED',
            'key': key,
            'value': check_type_value_node(after),
        }
    elif after is None:
        return {
            'type': 'ADDED',
            'key': key,
            'value': check_type_value_node(before),
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
            'value': check_type_value_node(after),
        }
    elif before != after:
        return {
            'type': 'CHANGEABLE',
            'key': key,
            'before_value': check_type_value_node(before),
            'after_value': check_type_value_node(after),
        }


def check_type_value_node(value_node):
    """Check sheet value type.

    Args:
        value_node: sheet value.

    Returns:
        value_node
    """
    if value_node is True:
        return 'true'
    if value_node is False:
        return 'false'
    return value_node