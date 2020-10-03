# -*- coding:utf-8 -*-

"""The templates formatting."""
from gendiff import (
    ADDED,
    CHANGEABLE,
    DELETED,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGEABLE,
)
from gendiff.nodes import get_children, get_name, get_status, get_value


def mapping_default(tree, name=None, status=None):  # noqa: WPS231
    """Return file differences without picking and sorting."""
    children = get_children(tree)

    if status is CHANGEABLE:
        return {
            '  + {0}'.format(name): get_value(tree).get(NEW_VALUE),
            '  - {0}'.format(name): get_value(tree).get(OLD_VALUE),
        }

    if not children:
        return get_value(tree)

    acc = {}
    for child in children:
        name = get_name(child)
        status = get_status(child)
        if status is ADDED:
            name = '  {0} {1}'.format('+', name)
        elif status is DELETED:
            name = '  {0} {1}'.format('-', name)
        elif status in (UNCHANGEABLE, None):  # noqa: WPS510
            name = '    {0}'.format(name)
        if status is CHANGEABLE:
            acc.update(mapping_default(child, name=name, status=status))
        else:
            acc.update({name: mapping_default(child)})
    return acc


def mapping_plain(tree):  # noqa: WPS210
    """Return maps for format plain."""
    acc = []

    def inner(node, path=None):  # noqa: WPS430, WPS210
        path = path if path else []
        children = get_children(node)
        current_value = get_value(node)

        if not children:
            path.append(current_value)
            return None

        for child in children:
            new_path = path.copy()
            name = get_name(child)
            status = get_status(child)

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
