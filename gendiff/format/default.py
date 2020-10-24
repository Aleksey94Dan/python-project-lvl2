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


def mapping_default(tree):
    """Return file differences without picking and sorting."""

    keys = tree.keys()

    for node in nodes:
        if node[nodes.STATUS]:
            print()

    # return acc


if __name__ == "__main__":
    from gendiff import files
    from gendiff import nodes
    from pprint import pprint
    old = files.load('tests/fixtures/nested_1.json')
    new = files.load('tests/fixtures/nested_2.yml')
    tree = nodes.make_tree(old, new)
    # pprint(tree)
    mapping_default(tree)
