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


def _flatten(subtree):
    acc = []
    for node in subtree:
        if isinstance(node, list):
            acc.extend(_flatten(node))
        else:
            acc.append(node)
    return acc


def mapping(node, key=None, ancestry=None):
    """Return maps for format plain."""
    ancestry = ancestry if ancestry else []
    status = node.get(nodes.STATUS)
    new_ancestry = ancestry.copy()
    new_ancestry.append(key)
    if status:
        return (
            '.'.join(filter(None, new_ancestry)),
            status,
            _helper(node.get(nodes.OLD_VALUE)),
            _helper(node.get(nodes.VALUE)),
        )
    paths = list(
        map(
            lambda original_values, original_keys: mapping(
                original_values,
                original_keys,
                new_ancestry,
            ),
            node.values(),
            node.keys(),
        ),
    )
    return sorted(_flatten(paths), reverse=True)


def format(source):  # noqa: A001, WPS210
    """Print plain."""
    string = []
    for package in source:
        origin, status, old_value, new_value = package
        string.append(
            _get_template(status).format(
                origin,
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
