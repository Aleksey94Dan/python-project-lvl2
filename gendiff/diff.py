# -*- coding:utf-8 -*-

"""Return the difference between two files."""

from gendiff.nodes import make_node, make_tree

ROOT = 'root'


def generate_diff(old, new, format):  # noqa: A002
    """
    Difference conclusion.

    Return the difference between two files according
    to the formatting function.
    """
    diff = make_node(
        name=ROOT,
        children=make_tree(old, new),
    )
    return format(diff)
