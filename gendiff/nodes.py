# -*- coding:utf-8 -*-


"""The module describes the rules for building AST."""
from operator import itemgetter

ADDED = 'added'
DELETED = 'deleted'
UNCHANGEABLE = 'unchangeable'
CHANGEABLE = 'changeable'
STATUS = 'status'
KEY = 'key'
VALUE = 'value'
NEW_VALUE = 'new_value'
OLD_VALUE = 'old_value'
CHILDREN = 'children'
NAME = 'name'


def make_node(name, status=None, children=None, current_value=None):
    """Return node."""
    return {
        NAME: name,
        STATUS: status,
        CHILDREN: children,
        VALUE: current_value,
    }


def make_tree(before_file, after_file):  # noqa: WPS210
    """Return an abstract syntax tree."""
    acc = []
    common_keys = before_file.keys() & after_file.keys()
    added_keys = after_file.keys() - before_file.keys()
    deleted_keys = before_file.keys() - after_file.keys()

    for common_key in common_keys:
        before_value = before_file.get(common_key)
        after_value = after_file.get(common_key)
        if isinstance(after_value, dict) and isinstance(before_value, dict):
            acc.append(
                make_node(
                    name=common_key,
                    children=make_tree(before_value, after_value),
                ),
            )
        elif after_value == before_value:
            acc.append(
                make_node(
                    name=common_key,
                    status=UNCHANGEABLE,
                    current_value=before_value,
                ),
            )
        else:
            acc.append(
                make_node(
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
            make_node(
                name=added_key,
                status=ADDED,
                current_value=after_file.get(added_key),
            ),
        )

    for deleted_key in deleted_keys:
        acc.append(
            make_node(
                name=deleted_key,
                status=DELETED,
                current_value=before_file.get(deleted_key),
            ),
        )
    acc.sort(key=itemgetter(NAME), reverse=False)
    return acc
