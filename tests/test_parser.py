# -*- coding:utf-8 -*-

"""Test for parse CLI."""

import argparse
import json

from gendiff import parsers
from tests.fixtures.expected import (
    EXPECTATION_FOR_NESTED_MAPPING_DEFAULT,
    EXPECTATION_NESTED_DEFAULT,
    EXPECTATION_PLAIN,
    cmd_format,
    extension,
    fake_flat,
    fake_format,
    filename_flat1,
    filename_flat2,
    filename_nested1,
    filename_nested2,
)


def test_parse():
    """Test CLI arguments."""
    actual_nested_default = parsers.parse(
        [
            cmd_format,
            extension[0],
            filename_nested1,
            filename_nested2,
        ],
    )
    actual_nested_plain = parsers.parse(
        [
            cmd_format,
            extension[2],
            filename_nested1,
            filename_nested2,
        ],
    )

    actual_nested_json = json.loads(
        parsers.parse(
            [
                cmd_format,
                extension[1],
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
                cmd_format,
                extension[1],
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
                cmd_format,
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
