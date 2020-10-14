# -*- coding:utf-8 -*-

"""Testing all modules to generate difference files."""

import json

import pytest

from gendiff import files, format
from gendiff.diff import generate_diff

FLAT1 = 'tests/fixtures/flat_files/file1.json'
FLAT2 = 'tests/fixtures/flat_files/file2.yml'
NESTED1 = 'tests/fixtures/nested_files/file1.json'
NESTED2 = 'tests/fixtures/nested_files/file2.yml'
FAKE_JSON = 'tests/fixtures/flat_files/file3.JSON'


def helper(path_to_file):
    """Read file."""
    with open(path_to_file) as exptected:
        return exptected.read()


@pytest.mark.parametrize('file1, file2, out_format, expectation', [
    (
        FLAT1,
        FLAT2,
        format.default,
        'tests/fixtures/expectation/expactation_flat_default.txt',
    ),
    (
        NESTED1,
        NESTED2,
        format.default,
        'tests/fixtures/expectation/expectation_nested_default.txt',
    ),
    (
        FLAT1,
        FLAT2,
        format.plain,
        'tests/fixtures/expectation/expactation_flat_plain.txt',
    ),
    (
        NESTED1,
        NESTED2,
        format.plain,
        'tests/fixtures/expectation/expectation_nested_plain.txt',
    ),
],
)
def test_stylish_and_plain(file1, file2, out_format, expectation):
    """Test default for flat and nested."""
    old = files.load(file1)
    new = files.load(file2)
    assert generate_diff(old, new, out_format) == helper(expectation)


@pytest.mark.parametrize('file1, file2, out_format, expectation', [
    (
        FLAT1,
        FLAT2,
        format.json,
        'tests/fixtures/expectation/expectation_flat_json.json',
    ),
    (
        NESTED1,
        NESTED2,
        format.json,
        'tests/fixtures/expectation/expactation_nested_json.json',
    ),
],
)
def test_json(file1, file2, out_format, expectation):
    """Test json for flat and nested.."""
    old = files.load(file1)
    new = files.load(file2)
    assert json.loads(generate_diff(old, new, out_format)) == json.loads(
        helper(expectation),
    )


@pytest.mark.parametrize('file1, file2, out_format, message', [
    (
        FLAT1,
        FAKE_JSON,
        format.json,
        'Unsupported .JSON extension',
    ),
],
)
def test_exception_extension(file1, file2, out_format, message):
    """Test exceptions for format and extension."""
    with pytest.raises(Exception, match=message):
        generate_diff(files.load(file1), files.load(file2), out_format)
