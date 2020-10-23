# -*- coding:utf-8 -*-


"""The module describes the rules for building Tree."""

ADDED = 'added'
DELETED = 'deleted'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
STATUS = 'status'
VALUE = 'value'
OLD_VALUE = 'old_value'


def _template(  # noqa: WPS211
    acc,
    added=None,
    deleted=None,
    common=None,
    old=None,
    new=None,
):
    if added:
        acc[added] = {
            STATUS: ADDED,
            VALUE: new.get(added),
        }
    if deleted:
        acc[deleted] = {
            STATUS: DELETED,
            VALUE: old.get(deleted),
        }
    if common:
        old_value = old.get(common)
        new_value = new.get(common)
        if all((isinstance(old_value, dict), isinstance(new_value, dict))):
            acc[common] = make_tree(old_value, new_value)
        elif new_value == old_value:
            acc[common] = {
                STATUS: UNCHANGED,
                VALUE: old_value,
            }
        else:
            acc[common] = {
                STATUS: CHANGED,
                VALUE: new_value,
                OLD_VALUE: old_value,
            }


def make_tree(old_file, new_file):  # noqa: WPS210
    """Return an abstract syntax tree."""
    acc = {}

    common_keys = old_file.keys() & new_file.keys()
    added_keys = new_file.keys() - old_file.keys()
    deleted_keys = old_file.keys() - new_file.keys()

    list(map(
        lambda added: _template(acc=acc, added=added, new=new_file),
        added_keys,
    ),
    )
    list(map(
        lambda deleted: _template(acc=acc, deleted=deleted, old=old_file),
        deleted_keys,
    ),
    )
    list(map(
        lambda common: _template(
            acc=acc,
            common=common,
            old=old_file,
            new=new_file,
        ),
        common_keys,
    ),
    )

    return acc
