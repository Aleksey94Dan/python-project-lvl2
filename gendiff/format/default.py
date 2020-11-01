# -*- coding:utf-8 -*-

"""Format default."""

from operator import itemgetter

from gendiff import nodes

SIGN = '    '

BY_THE_FIRST_LETTER = 4
BY_DIGIT = -1

_get_template = {
    nodes.ADDED: '  + {0}',
    nodes.DELETED: '  - {0}',
    nodes.CHANGED: ('  - {0}', '  + {0}'),
    nodes.UNCHANGED: '    {0}',
}.get


def _helper(node):
    if isinstance(node, (bool, int)):
        return str(node).lower()
    elif isinstance(node, str):
        return node
    elif node is None:
        return node
    return {
        '{0}{1}'.format(SIGN, original_key): _helper(original_value)
        if isinstance(original_value, dict) else original_value
        for original_key, original_value in node.items()
    }


def mapping(tree, indent=0):  # noqa: WPS210
    """Return file differences without picking and sorting."""
    acc = {}
    for k, v in tree.items():  # noqa: WPS111
        status = v.get(nodes.STATUS)
        new_value = _helper(v.get(nodes.VALUE))
        old_value = _helper(v.get(nodes.OLD_VALUE))
        if status == nodes.CHANGED:
            old, new = _get_template(status)
            acc[old.format(k)] = old_value
            acc[new.format(k)] = new_value
        elif status:
            acc[_get_template(status).format(k)] = new_value
        else:
            acc[_get_template(nodes.UNCHANGED).format(k)] = mapping(v)
    return acc


def _inner(node, indent=0):
    string = []
    for vertex in sorted(  # noqa: WPS352
        node.keys(),
        key=itemgetter(BY_THE_FIRST_LETTER, BY_DIGIT),
    ):
        child = node.get(vertex)
        if isinstance(child, dict):
            string.append('{0}{1}: {{\n'.format(indent * SIGN, vertex))
            string.append(_inner(child, indent + 1))
            string.append('{0}}}\n'.format((indent + 1) * SIGN))
        else:
            string.append('{0}{1}: {2}\n'.format(
                SIGN * indent, vertex, child,
            ),
            )
    return ''.join(string)


def format(tree):  # noqa: A001
    """Retrun default."""
    return '{{\n{0}}}'.format(_inner(tree))
