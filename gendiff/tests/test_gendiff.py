# -*- coding:utf-8 -*-

"""Test package."""

from gendiff.generate_diff import generate_diff


def test_json_flat_gendiff():
    """Function testing generate_diff for json."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff_flat.txt'
    path_to_first_file = 'gendiff/tests/fixtures/before.json'
    path_to_second_file = 'gendiff/tests/fixtures/after.json'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_yaml_flat_gendiff():
    """Function testing generate_diff for yaml."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff_flat.txt'
    path_to_first_file = 'gendiff/tests/fixtures/after.yaml'
    path_to_second_file = 'gendiff/tests/fixtures/before.yaml'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_json_inserted_gendiff():
    """Function testing generate_diff for json."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff_inserted'
    path_to_first_file = 'gendiff/tests/fixtures/after_inserted.json'
    path_to_second_file = 'gendiff/tests/fixtures/before_inserted.json'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_yaml_inserted_gendiff():
    """Function testing generate_diff for yaml."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff_inserted'
    path_to_first_file = 'gendiff/tests/fixtures/after_inserted.yaml'
    path_to_second_file = 'gendiff/tests/fixtures/before_inserted.yaml'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )
