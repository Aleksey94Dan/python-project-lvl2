# -*- coding:utf-8 -*-

"""Format plain."""

from gendiff import nodes

FOR_ADDED = "Property '{0}' was added with value: {1}"
FOR_DELETED = "Property '{0}' was removed"
FOR_CHANGED = "Property '{0}' was updated. From {1} to {2}"
COMPLEX_VALUE = '[complex value]'


def mapping(node, path=None, acc=None):  # noqa: WPS231
    """Return maps for format plain."""
    path = path if path else []
    acc = acc if acc else []
    for k, v in node.items():  # noqa: WPS111
        new_path = path.copy()
        new_path.append(k)
        if v.get(nodes.STATUS) == nodes.ADDED:
            new_path.append((nodes.ADDED, _helper(v.get(nodes.VALUE))))
        elif v.get(nodes.STATUS) == nodes.DELETED:
            new_path.append((nodes.DELETED, _helper(v.get(nodes.VALUE))))
        elif v.get(nodes.STATUS) == nodes.UNCHANGED:
            new_path.pop()
        elif v.get(nodes.STATUS) == nodes.CHANGED:
            new_path.append((
                nodes.CHANGED,
                _helper(v.get(nodes.OLD_VALUE)),
                _helper(v.get(nodes.VALUE)),
            ),
            )
        else:
            mapping(v, new_path, acc)
        acc.append(new_path)
    return acc


def format(source):  # noqa: A001, WPS231
    """Print plain."""
    string = []
    for package in sorted(source):
        if package:
            *origin, value_status = package
            origin = '.'.join(origin)
            if nodes.ADDED in value_status:
                string.append(FOR_ADDED.format(origin, value_status[1]))
            elif nodes.DELETED in value_status:
                string.append(FOR_DELETED.format(origin, value_status[1]))
            elif nodes.CHANGED in value_status:
                string.append(
                    FOR_CHANGED.format(
                        origin,
                        value_status[1],
                        value_status[2],
                    ),
                )
    return '\n'.join(string)


def _helper(arg1):
    if isinstance(arg1, (bool, int)):
        return str(arg1).lower()
    elif isinstance(arg1, dict):
        return COMPLEX_VALUE
    return "'{0}'".format(arg1)
