# -*- coding:utf-8 -*-


"""The module describes the rules for building AST."""

from gendiff import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    STATUS,
    UNCHANGEABLE,
    VALUE,
)


def mknode(name, status, children=[], value={}):  # noqa: WPS404, WPS110, B006
    """Return node."""
    return {
        NAME: name,
        STATUS: status,
        CHILDREN: children,
        VALUE: value,
    }
