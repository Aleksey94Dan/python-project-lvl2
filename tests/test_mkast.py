# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff import ROOT
from gendiff.nodes import mkast, mknode
from gendiff.parsers import get_data_from_file
from tests.fixtures.expected import (
    EXPECTATION_FLAT_AST,
    EXPECTATION_NESTED_AST,
)


def test_flat_mkast():
    """Flat file testing."""
    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'

    actual_json = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    filename1 = './tests/fixtures/flat_files/file1.yml'
    filename2 = './tests/fixtures/flat_files/file2.yml'

    actual_yml = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    assert EXPECTATION_FLAT_AST == actual_json
    assert EXPECTATION_FLAT_AST == actual_yml


def test_nested_mkast():
    """Nested file testing."""
    filename1 = './tests/fixtures/nested_files/file1.json'
    filename2 = './tests/fixtures/nested_files/file2.json'

    actual_json = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    filename1 = './tests/fixtures/nested_files/file1.yml'
    filename2 = './tests/fixtures/nested_files/file2.yml'

    actual_yml = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    assert EXPECTATION_NESTED_AST == actual_json
    assert EXPECTATION_NESTED_AST == actual_yml
