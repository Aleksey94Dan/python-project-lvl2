# -*- coding:utf-8 -*-

"""Format plain."""

from gendiff import ADDED, CHANGEABLE, DELETED, NEW_VALUE, OLD_VALUE

FOR_ADDED = "Property '{0}' was added with value: {1}\n"
FOR_DELETED = "Property '{0}' was removed\n"
FOR_CHANGEABLE = "Property '{0}' was updated. From {1} to {2}\n"
COMPLEX_VALUE = '[complex value]'


def format_(source):  # noqa: WPS231
    """Print plain."""
    string = ''
    for item in source:  # noqa: WPS110
        (path, current_value, status) = item

        if status is ADDED:
            if isinstance(current_value, (bool, int)):
                current_value = str(current_value).lower()
            elif isinstance(current_value, dict):
                current_value = COMPLEX_VALUE
            else:
                current_value = "'{0}'".format(current_value)
            string += FOR_ADDED.format(path, current_value)
        elif status is DELETED:
            string += FOR_DELETED.format(path)
        elif status is CHANGEABLE:
            if isinstance(current_value.get(OLD_VALUE), (bool, int)):
                current_value[OLD_VALUE] = str(  # noqa: WPS204
                    current_value[OLD_VALUE],
                ).lower()
            elif isinstance(current_value.get(OLD_VALUE), dict):
                current_value[OLD_VALUE] = COMPLEX_VALUE
            else:
                current_value[OLD_VALUE] = "'{0}'".format(
                    current_value[OLD_VALUE],
                )
            if isinstance(current_value.get(NEW_VALUE), (bool, int)):
                current_value[NEW_VALUE] = str(  # noqa: WPS204
                    current_value[NEW_VALUE],
                ).lower()
            elif isinstance(current_value.get(NEW_VALUE), dict):
                current_value[NEW_VALUE] = COMPLEX_VALUE
            else:
                current_value[NEW_VALUE] = "'{0}'".format(
                    current_value[NEW_VALUE],
                )
            string = string + FOR_CHANGEABLE.format(
                path,
                current_value.get(OLD_VALUE),
                current_value.get(NEW_VALUE),
            )
    return string
