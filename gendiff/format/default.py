# -*- coding:utf-8 -*-

"""Format default."""
from gendiff import nodes

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
    children = tree.get(nodes.CHILDREN)

    if status is nodes.CHANGEABLE:
        return {
            '  - {0}'.format(name): tree.get(nodes.VALUE).get(nodes.OLD_VALUE),
            '  + {0}'.format(name): tree.get(nodes.VALUE).get(nodes.NEW_VALUE),
        }

    if not children:
        return tree.get(nodes.VALUE)

    acc = {}
    for child in children:
        name = child.get(nodes.NAME)
        status = child.get(nodes.STATUS)
        if status == nodes.DELETED:
            name = '  {0} {1}'.format('-', name)
        elif status == nodes.ADDED:
            name = '  {0} {1}'.format('+', name)
        elif status in (nodes.UNCHANGEABLE, None):  # noqa: WPS510
            name = '    {0}'.format(name)
        if status == nodes.CHANGEABLE:
            acc.update(mapping_default(child, name=name, status=status))
        else:
            acc.update({name: mapping_default(child)})
    return acc
