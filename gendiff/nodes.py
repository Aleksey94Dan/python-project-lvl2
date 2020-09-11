# -*- coding:utf-8 -*-


"""The module describes the rules for building AST."""

from gendiff import (
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


def mknode(name, status=None, children=None, value=None):  # noqa: WPS110
    """Return node."""
    return {
        NAME: name,
        STATUS: status,
        CHILDREN: children,
        VALUE: value,
    }


def mkast(before_file, after_file, acc=None):  # noqa: WPS210
    """Rerurn an abstract syntax tree."""
    if acc is None:
        acc = []

    keys_before_change = set(before_file.keys())
    keys_after_cnange = set(after_file.keys())

    common_keys = keys_before_change.intersection(keys_after_cnange)
    added_keys = keys_after_cnange.difference(keys_before_change)
    deleted_keys = keys_before_change.difference(keys_after_cnange)

    for common_key in common_keys:
        before_value = before_file.get(common_key)
        after_value = after_file.get(common_key)
        if after_value == before_value:
            acc.append(
                mknode(
                    name=common_key,
                    status=UNCHANGEABLE,
                    value=before_value,
                ),
            )
        elif after_value != before_value:
            acc.append(
                mknode(
                    name=common_key,
                    status=CHANGEABLE,
                    value={OLD_VALUE: before_value, NEW_VALUE: after_value},
                ),
            )

    for added_key in added_keys:
        after_value = after_file.get(added_key)
        acc.append(
            mknode(
                name=added_key,
                status=ADDED,
                value=after_value,
            ),
        )

    for deleted_key in deleted_keys:
        before_value = before_file.get(deleted_key)
        acc.append(
            mknode(
                name=deleted_key,
                status=DELETED,
                value=before_value,
            ),
        )
    acc.sort(key=lambda name_of_key: name_of_key[NAME], reverse=False)
    return mknode(name='root', children=acc)
