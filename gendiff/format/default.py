# -*- coding:utf-8 -*-

"""The template for default formatting."""
from gendiff.nodes import get_children, get_name, get_value, get_status
from gendiff import (
    UNCHANGEABLE,
    CHANGEABLE,
    ADDED,
    DELETED,
    OLD_VALUE,
    NEW_VALUE,
)


def pretty_print(tree):  # noqa: D103, WPS210, WPS231
    children = get_children(tree)
    string = '{\n'
    for child in children:
        name = get_name(child)
        value = get_value(child)  # noqa: WPS110
        status = get_status(child)

        if isinstance(value, bool):
            value = str(value).lower()  # noqa: WPS110

        if status is ADDED:
            string = string + '  + {0}:{1}\n'.format(name, value)
        elif status is DELETED:
            string = string + '  - {0}:{1}\n'.format(name, value)
        elif status is UNCHANGEABLE:
            string = string + '    {0}:{1}\n'.format(name, value)
        elif status is CHANGEABLE:
            old_value = value.get(OLD_VALUE)
            new_value = value.get(NEW_VALUE)
            string = string + '  - {0}:{1}\n'.format(name, old_value)
            string = string + '  + {0}:{1}\n'.format(name, new_value)
    string = string + '}'  # noqa: WPS336
    return string
