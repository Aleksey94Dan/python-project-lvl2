# -*- coding:utf-8 -*-

"""Return the difference between two files."""

from gendiff import ROOT
from gendiff.nodes import mkast, mknode


def generate_diff(arg1, arg2, format_):
    """
    Difference conclusion.

    Return the difference between two files according
    to the formatting function.
    """
    diff = mknode(
        name=ROOT,
        children=mkast(arg1, arg2),
    )
    return format_(diff)
