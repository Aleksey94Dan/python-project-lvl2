# -*- coding:utf-8 -*-

"""Format default."""

SIGN = '  '


def _inner(node, indent=0, string=None):
    string = string if string else ''
    for vertex, child in node.items():
        vertex = SIGN + str(vertex) if ' ' not in str(vertex) else vertex
        child = str(child).lower() if isinstance(child, bool) else child
        if isinstance(child, dict):
            string = string + '{0}{1}: {{\n'.format(indent * SIGN, vertex)
            string = string + _inner(child, indent + 2)
            string = string + '{0}}}\n'.format((indent + 2) * SIGN)
        else:
            string = string + '{0}{1}: {2}\n'.format(
                SIGN * indent, str(vertex), str(child),
            )
    return string


def format(source):
    """Print default."""
    return '{{\n{0}}}\n'.format(_inner(source))
