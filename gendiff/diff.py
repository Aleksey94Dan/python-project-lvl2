# -*- coding:utf-8 -*-

"""Return the difference between two files."""

from gendiff import nodes


def generate_diff(old, new, format):  # noqa: A002
    """
    Difference conclusion.

    Return the difference between two files according
    to the formatting function.
    """
    diff = nodes.make_tree(old, new)
    return format(diff)
