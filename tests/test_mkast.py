# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff import ROOT
from gendiff.nodes import mkast, mknode
from gendiff.parsers import get_data_from_file
from tests.fixtures.expected import (
    EXPECTATION_FLAT_AST,
    EXPECTATION_NESTED_AST,
    filename_flat1,
    filename_flat2,
    filename_nested1,
    filename_nested2,
)


def test_mkast():
    """Flat and nested files testing."""
    actual_flat = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename_flat1),
            get_data_from_file(filename_flat2),
        ),
    )

    actual_nested = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename_nested1),
            get_data_from_file(filename_nested2),
        ),
    )

    assert EXPECTATION_NESTED_AST == actual_nested
    assert EXPECTATION_FLAT_AST == actual_flat
