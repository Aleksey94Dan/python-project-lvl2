# -*- coding:utf-8 -*-

"""Test package."""

from gendiff.generate_diff import generate_diff
from gendiff.tests.expected import FLAT_GENDIFF, INSERTED_GENDIFF


def test_json_flat_gendiff():
    """Function testing generate_diff for json."""
    path_to_first_file = 'gendiff/tests/fixtures/before.json'
    path_to_second_file = 'gendiff/tests/fixtures/after.json'
    expected_data = FLAT_GENDIFF
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_yaml_flat_gendiff():
    """Function testing generate_diff for yaml."""
    path_to_first_file = 'gendiff/tests/fixtures/before.yaml'
    path_to_second_file = 'gendiff/tests/fixtures/after.yaml'
    expected_data = FLAT_GENDIFF
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_json_inserted_gendiff():
    """Function testing generate_diff for json."""
    path_to_first_file = 'gendiff/tests/fixtures/before_inserted.json'
    path_to_second_file = 'gendiff/tests/fixtures/after_inserted.json'
    expected_data = INSERTED_GENDIFF
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_yaml_inserted_gendiff():
    """Function testing generate_diff for yaml."""
    path_to_first_file = 'gendiff/tests/fixtures/before_inserted.yaml'
    path_to_second_file = 'gendiff/tests/fixtures/after_inserted.yaml'
    expected_data = INSERTED_GENDIFF
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )
