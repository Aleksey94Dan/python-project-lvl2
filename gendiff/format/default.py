# -*- coding:utf-8 -*-

"""Format default."""

from operator import itemgetter

from gendiff import nodes

SIGN = '    '


def _transform(node):
    if isinstance(node, (bool, int)):
        return str(node).lower()
    elif isinstance(node, str):
        return node
    res = {}
    for k, v in node.items():  # noqa: WPS111
        if isinstance(v, dict):
            res['{0}{1}'.format(SIGN, k)] = _transform(v)
        else:
            res['{0}{1}'.format(SIGN, k)] = v
    return res


def mapping(tree, indent=0):  # noqa: WPS231
    """Return file differences without picking and sorting."""
    acc = {}
    for k, v in tree.items():  # noqa: WPS111
        if v.get(nodes.STATUS) == nodes.ADDED:
            acc['  + {0}'.format(k)] = _transform(v[nodes.VALUE])
        elif v.get(nodes.STATUS) == nodes.DELETED:
            acc['  - {0}'.format(k)] = _transform(v[nodes.VALUE])
        elif v.get(nodes.STATUS) == nodes.UNCHANGED:
            acc['    {0}'.format(k)] = _transform(v[nodes.VALUE])
        elif v.get(nodes.STATUS) == nodes.CHANGED:
            acc['  - {0}'.format(k)] = _transform(v[nodes.OLD_VALUE])
            acc['  + {0}'.format(k)] = _transform(v[nodes.VALUE])
        else:
            acc['    {0}'.format(k)] = mapping(v)
    return acc


def _inner(node, indent=0):
    string = []
    for vertex in sorted(node.keys(), key=itemgetter(4, -1)):
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
