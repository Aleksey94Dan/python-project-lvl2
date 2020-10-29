# -*- coding:utf-8 -*-

"""Format plain."""

from gendiff import nodes

COMPLEX_VALUE = '[complex value]'


_get_template = {
    nodes.ADDED: "Property '{0}' was added with value: {1}",
    nodes.DELETED: "Property '{0}' was removed",
    nodes.CHANGED: "Property '{0}' was updated. From {2} to {1}",
    nodes.UNCHANGED: '',
}.get


def mapping(node, path=None, acc=None):  # noqa: WPS210
    """Return maps for format plain."""
    path = path if path else []
    acc = acc if acc else []
    for k, v in sorted(node.items(), reverse=True):  # noqa: WPS111
        new_path = path.copy()
        new_path.append(k)
        status = v.get(nodes.STATUS)
        if status:
            new_path.append((
                status,
                _helper(v.get(nodes.OLD_VALUE)),
                _helper(v.get(nodes.VALUE)),
            ),
            )
        elif isinstance(v, dict):
            mapping(v, new_path, acc)
        acc.append(new_path)
    return acc


def format(source):  # noqa: A001, WPS210
    """Print plain."""
    source = filter(lambda x: isinstance(x[-1], tuple), source)  # noqa: WPS111
    string = []
    for package in source:
        *origin, (status, old_value, new_value) = package  # noqa: WPS414
        string.append(
            _get_template(status).format(
                '.'.join(origin),
                new_value,
                old_value,
            ),
        )
    string.reverse()
    return '\n'.join(filter(None, string))


def _helper(arg1):
    if isinstance(arg1, (bool, int)):
        return str(arg1).lower()
    elif isinstance(arg1, dict):
        return COMPLEX_VALUE
    return "'{0}'".format(arg1)

