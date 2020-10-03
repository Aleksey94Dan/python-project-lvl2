# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff import ROOT
from gendiff.nodes import mkast, mknode
from gendiff.parsers import get_data_from_file
from tests.fixtures.expected import (
    EXPECTATION_NESTED_AST,
    filename_nested1,
    filename_nested2,
)


def test_mkast():
    """Nested files testing."""
    actual = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename_nested1),
            get_data_from_file(filename_nested2),
        ),
    )

    assert EXPECTATION_NESTED_AST == actual
