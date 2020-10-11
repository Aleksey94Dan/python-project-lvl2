# -*- coding:utf-8 -*-

"""Format plain."""

from gendiff import ADDED, CHANGEABLE, DELETED, NEW_VALUE, OLD_VALUE

FOR_ADDED = "Property '{0}' was added with value: {1}\n"
FOR_DELETED = "Property '{0}' was removed\n"
FOR_CHANGEABLE = "Property '{0}' was updated. From {1} to {2}\n"
COMPLEX_VALUE = '[complex value]'


def _helper(arg1):
    if isinstance(arg1, (bool, int)):
        return str(arg1).lower()
    elif isinstance(arg1, dict):
        return COMPLEX_VALUE
    return "'{0}'".format(arg1)


def format(source):
    """Print plain."""
    string = ''
    for values_item in source:
        (path, current_value, status) = values_item

        if status is ADDED:
            current_value = _helper(current_value)
            string += FOR_ADDED.format(path, current_value)
        elif status is DELETED:
            string += FOR_DELETED.format(path)
        elif status is CHANGEABLE:
            current_value[OLD_VALUE] = _helper(current_value[OLD_VALUE])
            current_value[NEW_VALUE] = _helper(current_value[NEW_VALUE])
            string = string + FOR_CHANGEABLE.format(
                path,
                current_value.get(OLD_VALUE),
                current_value.get(NEW_VALUE),
            )
    return string
