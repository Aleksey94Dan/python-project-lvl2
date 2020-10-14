# -*- coding:utf-8 -*-

"""Format default."""
from gendiff.nodes import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    STATUS,
    UNCHANGEABLE,
    VALUE,
)

SIGN = '    '


def _inner(node, indent=0):
    string = []
    for vertex, child in node.items():
        vertex = SIGN + str(vertex) if ' ' not in str(vertex) else vertex
        child = str(child).lower() if isinstance(child, bool) else child
        if isinstance(child, dict):
            string.append('{0}{1}: {{\n'.format(indent * SIGN, vertex))
            string.append(_inner(child, indent + 1))
            string.append('{0}}}\n'.format((indent + 1) * SIGN))
        else:
            string.append('{0}{1}: {2}\n'.format(
                SIGN * indent, str(vertex), str(child),
            ),
            )
    return ''.join(string)


def format(source):  # noqa: A001
    """Print default."""
    return '{{\n{0}}}\n'.format(_inner(source))


def mapping_default(tree, name=None, status=None):  # noqa: WPS231
    """Return file differences without picking and sorting."""
    children = tree.get(CHILDREN)

    if status is CHANGEABLE:
        return {
            '  - {0}'.format(name): tree.get(VALUE).get(OLD_VALUE),
            '  + {0}'.format(name): tree.get(VALUE).get(NEW_VALUE),
        }

    if not children:
        return tree.get(VALUE)

    acc = {}
    for child in children:
        name = child.get(NAME)
        status = child.get(STATUS)
        if status is DELETED:
            name = '  {0} {1}'.format('-', name)
        elif status is ADDED:
            name = '  {0} {1}'.format('+', name)
        elif status in (UNCHANGEABLE, None):  # noqa: WPS510
            name = '    {0}'.format(name)
        if status is CHANGEABLE:
            acc.update(mapping_default(child, name=name, status=status))
        else:
            acc.update({name: mapping_default(child)})
    return acc
