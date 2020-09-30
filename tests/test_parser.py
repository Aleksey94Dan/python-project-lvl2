# -*- coding:utf-8 -*-

"""Test for parse CLI."""

import argparse
import json

from gendiff import parsers
from tests.fixtures.expected import (
    EXPECTATION_FOR_NESTED_MAPPING_DEFAULT,
    EXPECTATION_NESTED_DEFAULT,
    EXPECTATION_PLAIN,
)

filename_flat1 = 'tests/fixtures/flat_files/file1.yml'
filename_flat2 = 'tests/fixtures/flat_files/file2.json'
filename_nested1 = 'tests/fixtures/nested_files/file1.json'
filename_nested2 = 'tests/fixtures/nested_files/file2.yml'
fake_flat = 'tests/fixtures/flat_files/file1.ymls'
fake_format = 'ini'


def test_parse():
    """Test CLI arguments."""
    actual_nested_default = parsers.parse(
        [
            '-f',
            'default',
            filename_nested1,
            filename_nested2,
        ],
    )
    actual_nested_plain = parsers.parse(
        [
            '-f',
            'plain',
            filename_nested1,
            filename_nested2,
        ],
    )

    actual_nested_json = json.loads(
        parsers.parse(
            [
                '-f',
                'json',
                filename_nested1,
                filename_nested2,
            ],
        ),
    )

    for actual_nested in actual_nested_default.split('\n'):
        assert actual_nested in EXPECTATION_NESTED_DEFAULT

    for actual_plain in actual_nested_plain.split('\n'):
        assert actual_plain in EXPECTATION_PLAIN

    assert actual_nested_json == EXPECTATION_FOR_NESTED_MAPPING_DEFAULT


def test_argument_type_error_extension():
    """Test for invalid extension."""
    try:
        parsers.parse(
            [
                '-f',
                'json',
                fake_flat,
                filename_flat1,
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
        parsers.parse(
            [
                '-f',
                fake_format,
                filename_flat1,
                filename_flat2,
            ],
        )
    except SystemExit as exinfo:
        assert isinstance(
            exinfo.__context__,  # noqa: WPS609
            argparse.ArgumentError,
        )
    else:
        raise ValueError('Exception not raised')
