# -*- coding:utf-8 -*-

"""The module describes the rules for building nodes."""


def generate_ast(before_file, after_file):
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
            'Identifier': 'ADDED',
            'Key': key,
            'Value': check_type_value_node(after),
        }
    elif after is None:
        return {
            'Identifier': 'DELETED',
            'Key': key,
            'Value': check_type_value_node(before),
        }
    elif isinstance(before, dict) and isinstance(after, dict):
        return {
            'Identifier': 'PARENT',
            'Key': key,
            'Child': generate_ast(before, after),
        }
    elif before == after:
        return {
            'Identifier': 'UNCHANGEABLE',
            'Key': key,
            'Value': check_type_value_node(after),
        }
    elif before != after:
        return {
            'Identifier': 'CHANGEABLE',
            'Key': key,
            'Before_value': check_type_value_node(before),
            'After_value': check_type_value_node(after),
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
