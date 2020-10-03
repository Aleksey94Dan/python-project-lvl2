# -*- coding:utf-8 -*-


"""The module describes the rules for building AST."""
from operator import itemgetter

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


def mknode(name, status=None, children=None, current_value=None):
    """Return node."""
    return {
        NAME: name,
        STATUS: status,
        CHILDREN: children,
        VALUE: current_value,
    }


def get_children(node):
    """Return children of node."""
    return node.get(CHILDREN)


def get_name(node):
    """Return name of node."""
    return node.get(NAME)


def get_value(node):
    """Return value of node."""
    return node.get(VALUE)


def get_status(node):
    """Return status of node."""
    return node.get(STATUS)


def mkast(before_file, after_file):  # noqa: WPS210
    """Return an abstract syntax tree."""
    acc = []

    keys_before_change = set(before_file.keys())
    keys_after_change = set(after_file.keys())

    common_keys = keys_before_change.intersection(keys_after_change)
    added_keys = keys_after_change.difference(keys_before_change)
    deleted_keys = keys_before_change.difference(keys_after_change)

    for common_key in common_keys:
        before_value = before_file.get(common_key)
        after_value = after_file.get(common_key)
        if isinstance(after_value, dict) and isinstance(before_value, dict):
            acc.append(
                mknode(
                    name=common_key,
                    children=mkast(before_value, after_value),
                ),
            )
        elif after_value == before_value:
            acc.append(
                mknode(
                    name=common_key,
                    status=UNCHANGEABLE,
                    current_value=before_value,
                ),
            )
        else:
            acc.append(
                mknode(
                    name=common_key,
                    status=CHANGEABLE,
                    current_value={
                        OLD_VALUE: before_value,
                        NEW_VALUE: after_value,
                    },
                ),
            )

    for added_key in added_keys:
        acc.append(
            mknode(
                name=added_key,
                status=ADDED,
                current_value=after_file.get(added_key),
            ),
        )

    for deleted_key in deleted_keys:
        acc.append(
            mknode(
                name=deleted_key,
                status=DELETED,
                current_value=before_file.get(deleted_key),
            ),
        )
    acc.sort(key=itemgetter(NAME), reverse=False)
    return acc
