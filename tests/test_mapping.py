# -*- coding:utf-8 -*-

"""Test for format."""
from gendiff.nodes import mknode, mkast
from gendiff.format.mapping import mapping_default, mapping_plain
from gendiff.parsers import get_data_from_file
from gendiff import ROOT
from tests.fixtures.expected import (
    EXPECTATION_FOR_FLAT_MAPPING_DEFAULT,
    EXPECTATION_FOR_NESTED_MAPPING_DEFAULT,
    EXPECTATION_FOR_FLAT_MAPPING_PLAIN,
    EXPECTATION_FOR_NESTED_MAPPING_PLAIN,
)


def test_mapping_format_defatult():
    """Test mapping for flat and nested files."""
    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'

    actual_flat = mapping_default(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )

    filename1 = './tests/fixtures/nested_files/file1.json'
    filename2 = './tests/fixtures/nested_files/file2.json'

    actual_nested = mapping_default(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )
    assert EXPECTATION_FOR_FLAT_MAPPING_DEFAULT == actual_flat
    assert EXPECTATION_FOR_NESTED_MAPPING_DEFAULT == actual_nested


def test_mapping_format_plain():  # noqa: WPS210
    """Test mapping for flat and nested files."""
    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'

    actual_flats = mapping_plain(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )

    for actual_flat in actual_flats:
        assert actual_flat in EXPECTATION_FOR_FLAT_MAPPING_PLAIN

    filename1 = './tests/fixtures/nested_files/file1.json'
    filename2 = './tests/fixtures/nested_files/file2.json'

    actual_nesteds = mapping_plain(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )

    for actual_nested in actual_nesteds:
        assert actual_nested in EXPECTATION_FOR_NESTED_MAPPING_PLAIN
