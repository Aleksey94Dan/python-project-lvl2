# -*- coding:utf-8 -*-

"""Format plain."""

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

FOR_ADDED = "Property '{0}' was added with value: {1}"
FOR_DELETED = "Property '{0}' was removed"
FOR_CHANGEABLE = "Property '{0}' was updated. From {1} to {2}"
COMPLEX_VALUE = '[complex value]'


def mapping_plain(tree):  # noqa: WPS210
    """Return maps for format plain."""
    acc = []

    def inner(node, path=None):  # noqa: WPS430, WPS210
        path = path if path else []
        children = node.get(CHILDREN)
        current_value = node.get(VALUE)

        if not children:
            path.append(current_value)
            return None

        for child in children:
            new_path = path.copy()
            name = child.get(NAME)
            status = child.get(STATUS)

            if child:
                if name not in path:
                    new_path.append(name)
                    inner(child, new_path)
                if status is not None:
                    new_path.append(status)
                    acc.append(new_path)
        return list(
            map(
                lambda key_for_plain: (
                    '.'.join(key_for_plain[:-2]),
                    key_for_plain[-2],
                    key_for_plain[-1],
                ),
                filter(
                    lambda key_for_plain:
                        key_for_plain and UNCHANGEABLE not in key_for_plain,
                    acc,
                ),
            ),
        )
    return inner(tree)


def _helper(arg1):
    if isinstance(arg1, (bool, int)):
        return str(arg1).lower()
    elif isinstance(arg1, dict):
        return COMPLEX_VALUE
    return "'{0}'".format(arg1)


def format(source):  # noqa: A001
    """Print plain."""
    string = []
    for values_item in source:
        (path, current_value, status) = values_item

        if status is ADDED:
            current_value = _helper(current_value)
            string.append(FOR_ADDED.format(path, current_value))
        elif status is DELETED:
            string.append(FOR_DELETED.format(path))
        elif status is CHANGEABLE:
            current_value[OLD_VALUE] = _helper(current_value[OLD_VALUE])
            current_value[NEW_VALUE] = _helper(current_value[NEW_VALUE])
            string.append(FOR_CHANGEABLE.format(
                path,
                current_value.get(OLD_VALUE),
                current_value.get(NEW_VALUE),
            ))
    return '\n'.join(string)
