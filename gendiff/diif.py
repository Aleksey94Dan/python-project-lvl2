# -*- coding:utf-8 -*-

"""Return the difference between two files."""

from gendiff import ROOT
from gendiff.nodes import make_tree, make_node


def generate_diff(arg1, arg2, format):
    """
    Difference conclusion.

    Return the difference between two files according
    to the formatting function.
    """
    diff = make_node(
        name=ROOT,
        children=make_tree(arg1, arg2),
    )
    return format(diff)
