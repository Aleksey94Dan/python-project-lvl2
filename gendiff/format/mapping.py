# -*- coding:utf-8 -*-

"""The templates formatting."""
from gendiff import (
    ADDED,
    CHANGEABLE,
    DELETED,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGEABLE,
    CHILDREN,
    VALUE,
    NAME,
    STATUS,
)


def mapping_default(tree, name=None, status=None):  # noqa: WPS231
    """Return file differences without picking and sorting."""
    children = tree.get(CHILDREN)

    if status is CHANGEABLE:
        return {
            '  + {0}'.format(name): tree.get(VALUE).get(NEW_VALUE),
            '  - {0}'.format(name): tree.get(VALUE).get(OLD_VALUE),
        }

    if not children:
        return tree.get(VALUE)

    acc = {}
    for child in children:
        name = child.get(NAME)
        status = child.get(STATUS)
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
