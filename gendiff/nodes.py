# -*- coding:utf-8 -*-


"""The module describes the rules for building Tree."""

ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
STATUS = 'status'
VALUE = 'value'
OLD_VALUE = 'old_value'


def _template(acc, key=None, old=None, new=None):
    if old:
        acc[key] = {  # noqa: WPS204
            STATUS: DELETED,
            VALUE: old.get(key),
        }
    if new:
        acc[key] = {
            STATUS: ADDED,
            VALUE: new.get(key),
        }
    if all((old, new)):
        old_value = old.get(key)
        new_value = new.get(key)
        if all((isinstance(old_value, dict), isinstance(new_value, dict))):
            acc[key] = make_tree(old_value, new_value)
        elif new_value == old_value:
            acc[key] = {
                STATUS: UNCHANGED,
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

    common_keys = old_file.keys() & new_file.keys()
    added_keys = new_file.keys() - old_file.keys()
    deleted_keys = old_file.keys() - new_file.keys()

    list(map(
        lambda added: _template(acc=acc, key=added, new=new_file),
        added_keys,
    ),
    )
    list(map(
        lambda deleted: _template(acc=acc, key=deleted, old=old_file),
        deleted_keys,
    ),
    )
    list(map(
        lambda common: _template(
            acc=acc,
            key=common,
            old=old_file,
            new=new_file,
        ),
        common_keys,
    ),
    )

    return acc
