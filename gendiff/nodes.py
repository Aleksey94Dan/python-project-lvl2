# -*- coding:utf-8 -*-


"""The module describes the rules for building Tree."""

ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
STATUS = 'status'
VALUE = 'value'
OLD_VALUE = 'old_value'


def make_tree(old_file, new_file):  # noqa: WPS210
    """Return an abstract syntax tree."""
    acc = {}

    for common_key in old_file.keys() & new_file.keys():
        old_value = old_file.get(common_key)
        new_value = new_file.get(common_key)

        if all((isinstance(old_value, dict), isinstance(new_value, dict))):
            acc[common_key] = make_tree(old_value, new_value)
        elif new_value == old_value:
            acc[common_key] = {
                STATUS: UNCHANGED,
                VALUE: old_value,
            }
        else:
            acc[common_key] = {
                STATUS: CHANGED,
                VALUE: new_value,
                OLD_VALUE: old_value,
            }

    for added_key in new_file.keys() - old_file.keys():
        acc[added_key] = {
            STATUS: ADDED,
            VALUE: new_file.get(added_key),
        }

    for deleted_key in old_file.keys() - new_file.keys():
        acc[deleted_key] = {
            STATUS: DELETED,
            VALUE: old_file.get(deleted_key),
        }
    return acc
