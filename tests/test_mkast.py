# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff import ROOT
from gendiff.nodes import make_tree, make_node
from gendiff.files import load
from tests.fixtures.expected import (
    EXPECTATION_NESTED_AST,
    filename_nested1,
    filename_nested2,
)


def test_make_tree():
    """Nested files testing."""
    actual = make_node(
        name=ROOT,
        children=make_tree(
            load(filename_nested1),
            load(filename_nested2),
        ),
    )

    assert EXPECTATION_NESTED_AST == actual
