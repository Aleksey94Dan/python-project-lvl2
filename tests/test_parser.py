# -*- coding:utf-8 -*-

"""Test for parse CLI."""

import argparse

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


def test_argument_type_error_extension():
    """Test for invalid extension."""
    try:
        parse(
            [
                '-f',
                'json',
                'tests/fixtures/flat_files/file1.ymls',
                'tests/fixtures/flat_files/file2.json',
            ],
        )
    except SystemExit as exinfo:
        assert isinstance(
            exinfo.__context__,  # noqa: WPS609
            argparse.ArgumentError,
        )
    else:
        raise ValueError('Exception not raised')


def test_argument_type_error_formatter():
    """Test for invalid format."""
    try:
        parse(
            [
                '-f',
                'ini',
                'tests/fixtures/flat_files/file1.json',
                'tests/fixtures/flat_files/file2.json',
            ],
        )
    except SystemExit as exinfo:
        assert isinstance(
            exinfo.__context__,  # noqa: WPS609
            argparse.ArgumentError,
        )
    else:
        raise ValueError('Exception not raised')
