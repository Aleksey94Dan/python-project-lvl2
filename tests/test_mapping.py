# -*- coding:utf-8 -*-

"""Test for format."""
from gendiff import ROOT
from gendiff.format.mapping import mapping_default, mapping_plain
from gendiff.nodes import mkast, mknode
from gendiff.parsers import get_data_from_file
from tests.fixtures.expected import (
    EXPECTATION_FOR_NESTED_MAPPING_DEFAULT,
    EXPECTATION_FOR_NESTED_MAPPING_PLAIN,
    filename_nested1,
    filename_nested2,
)


def test_mapping_format_defatult():
    """Test mapping for flat and nested files."""
    actual_nested = mapping_default(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename_nested1),
                get_data_from_file(filename_nested2),
            ),
        ),
    )
    assert EXPECTATION_FOR_NESTED_MAPPING_DEFAULT == actual_nested


def test_mapping_format_plain():
    """Test mapping for flat and nested files."""
    actual_nesteds = mapping_plain(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename_nested1),
                get_data_from_file(filename_nested2),
            ),
        ),
    )
    for actual_nested in actual_nesteds:
        assert actual_nested in EXPECTATION_FOR_NESTED_MAPPING_PLAIN
