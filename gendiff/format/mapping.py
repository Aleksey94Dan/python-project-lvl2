# -*- coding:utf-8 -*-

"""The template for default formatting."""
from gendiff.nodes import (
    get_children,
    get_name,
    get_value,
    get_status,
)
from gendiff import (
    UNCHANGEABLE,
    CHANGEABLE,
    ADDED,
    DELETED,
    OLD_VALUE,
    NEW_VALUE,
)


def get_mapping(tree, name=None, status=None):  # noqa: WPS210, WPS231
    """Return file differences without picking and sorting."""
    children = get_children(tree)
    current_value = get_value(tree)

    if status is CHANGEABLE:
        return {
            '  + {0}'.format(name): current_value.get(NEW_VALUE),
            '  - {0}'.format(name): current_value.get(OLD_VALUE),
        }

    if not children:
        return current_value

    acc = {}
    for child in children:
        name = get_name(child)
        status = get_status(child)
        if status is ADDED:  # noqa: WPS223
            name = '  {0} {1}'.format('+', name)
        elif status is DELETED:
            name = '  {0} {1}'.format('-', name)
        elif status is UNCHANGEABLE:
            name = '    {0}'.format(name)
        elif status is None:
            name = '    {0}'.format(name)
        elif status is CHANGEABLE:
            acc.update(get_mapping(child, name=name, status=status))
        acc.update({name: get_mapping(child)})
    return acc
