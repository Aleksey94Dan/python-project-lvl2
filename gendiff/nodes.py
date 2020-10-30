# -*- coding:utf-8 -*-


"""The module describes the rules for building Tree."""

ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
STATUS = 'status'
VALUE = 'value'
OLD_VALUE = 'old_value'


def _get_node(acc, key=None, old_value=None, new_value=None):

    if all((isinstance(old_value, dict), isinstance(new_value, dict))):
        acc[key] = make_tree(old_value, new_value)  # noqa: WPS204
    elif new_value == old_value:
        acc[key] = {
            STATUS: UNCHANGED,
            VALUE: old_value,
        }
    elif old_value is None:
        acc[key] = {
            STATUS: ADDED,
            VALUE: new_value,
        }
    elif new_value is None:
        acc[key] = {
            STATUS: DELETED,
            VALUE: old_value,
        }
    else:
        acc[key] = {
            STATUS: CHANGED,
            VALUE: new_value,
            OLD_VALUE: old_value,
        }


def make_tree(old_file, new_file):
    """Return an abstract syntax tree."""
    acc = {}

    original_keys = old_file.keys() | new_file.keys()

    list(map(
        lambda key: _get_node(
            acc=acc,
            key=key,
            old_value=old_file.get(key),
            new_value=new_file.get(key),
        ),
        original_keys,
    ),
    )
    return acc
