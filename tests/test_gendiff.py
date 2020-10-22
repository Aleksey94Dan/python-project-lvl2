# -*- coding:utf-8 -*-

"""Testing all modules to generate difference files."""

import json

import pytest

from gendiff import files, format
from gendiff.diff import generate_diff

FLAT1 = 'tests/fixtures/flat_1.json'
FLAT2 = 'tests/fixtures/flat_2.yml'
NESTED1 = 'tests/fixtures/nested_1.json'
NESTED2 = 'tests/fixtures/nested_2.yml'
FAKE_JSON = 'tests/fixtures/fake.JSON'
EMPTY_JSON = 'tests/fixtures/empty.json'
UNCORRECT_YML = 'tests/fixtures/uncorrect.yml'
FLAT_OUT_DEFAULT = 'tests/fixtures/flat_out_default.txt'
FLAT_OUT_PLAIN = 'tests/fixtures/flat_out_plain.txt'
FLAT_OUT_JSON = 'tests/fixtures/flat_out_json.json'
NESTED_OUT_DEFAULT = 'tests/fixtures/nested_out_default.txt'
NESTED_OUT_PLAIN = 'tests/fixtures/nested_out_plain.txt'
NESTED_OUT_JSON = 'tests/fixtures/nested_out_json.json'
ERROR_MESSAGE1 = 'Unsupported .JSON extension'
ERROR_MESSAGE2 = (
    'Incorrect structure files. '
    'Become familiar with the JSON/YML compilation rules.'  # noqa: WPS326
)


def read(path_to_file):
    """Read file."""
    with open(path_to_file) as exptected:
        return exptected.read()


@pytest.mark.parametrize('file1, file2, out_format, expectation', [
    (FLAT1, FLAT2, format.default, FLAT_OUT_DEFAULT),
    (NESTED1, NESTED2, format.default, NESTED_OUT_DEFAULT),
    (FLAT1, FLAT2, format.plain, FLAT_OUT_PLAIN),
    (NESTED1, NESTED2, format.plain, NESTED_OUT_PLAIN),
],
)
def test_stylish_and_plain(file1, file2, out_format, expectation):
    """Test default for flat and nested."""
    old = files.load(file1)
    new = files.load(file2)
    assert generate_diff(old, new, out_format) == read(expectation)


@pytest.mark.parametrize('file1, file2, out_format, expectation', [
    (FLAT1, FLAT2, format.json, FLAT_OUT_JSON),
    (NESTED1, NESTED2, format.json, NESTED_OUT_JSON),
],
)
def test_json(file1, file2, out_format, expectation):
    """Test json for flat and nested.."""
    old = files.load(file1)
    new = files.load(file2)
    assert json.loads(generate_diff(old, new, out_format)) == json.loads(
        read(expectation),
    )


@pytest.mark.parametrize('file1, file2, out_format, message', [
    (FLAT1, FAKE_JSON, format.json, ERROR_MESSAGE1),
    (EMPTY_JSON, EMPTY_JSON, format.json, ERROR_MESSAGE2),
    (UNCORRECT_YML, UNCORRECT_YML, format.json, ERROR_MESSAGE2),
],
)
def test_exception(file1, file2, out_format, message):
    """Test exceptions for format and extension."""
    with pytest.raises(Exception, match=message):
        generate_diff(files.load(file1), files.load(file2), out_format)
