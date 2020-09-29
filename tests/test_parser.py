# -*- coding:utf-8 -*-

"""Test for parse CLI."""

from gendiff.parsers import parse
from tests.fixtures.expected import (
    EXPECTATION_FLAT_DEFAULT,
    EXPECTATION_JSON,
    EXPECTATION_NESTED_DEFAULT,
    EXPECTATION_PLAIN,
)


def test_parse():
    """Test CLI arguments."""
    actual_flat_default = parse(
        [
            '-f',
            'default',
            'tests/fixtures/flat_files/file1.yml',
            'tests/fixtures/flat_files/file2.json',
        ],
    )
    actual_nested_default = parse(
        [
            '-f',
            'default',
            'tests/fixtures/nested_files/file1.json',
            'tests/fixtures/nested_files/file2.json',
        ],
    )
    actual_nested_plain = parse(
        [
            '-f',
            'plain',
            'tests/fixtures/nested_files/file1.yml',
            'tests/fixtures/nested_files/file2.json',
        ],
    )

    actual_nested_json = parse(
        [
            '-f',
            'json',
            'tests/fixtures/nested_files/file1.json',
            'tests/fixtures/nested_files/file2.json',
        ],
    )

    for actual in actual_flat_default.split('\n'):
        assert actual in EXPECTATION_FLAT_DEFAULT

    for actual in actual_nested_default.split('\n'):
        assert actual in EXPECTATION_NESTED_DEFAULT

    for actual in actual_nested_plain.split('\n'):
        assert actual in EXPECTATION_PLAIN

    for actual in actual_nested_json.split(','):
        assert actual in EXPECTATION_JSON
