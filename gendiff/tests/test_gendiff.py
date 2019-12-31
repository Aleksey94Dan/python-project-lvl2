# -*- coding:utf-8 -*-

"""Test package."""

from gendiff.generate_diff import generate_diff, get_files


def test_json_gendiff():
    """Function testing generate_diff for json."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff.txt'
    path_to_first_file = 'gendiff/tests/fixtures/after.json'
    path_to_second_file = 'gendiff/tests/fixtures/before.json'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )


def test_yaml_gendiff():
    """Function testing generate_diff for yaml."""
    path_to_expected_file = 'gendiff/tests/fixtures/diff.txt'
    path_to_first_file = 'gendiff/tests/fixtures/after.yaml'
    path_to_second_file = 'gendiff/tests/fixtures/before.yaml'
    with open(path_to_expected_file) as diff_file:
        expected_data = diff_file.read()
    assert expected_data == generate_diff(
        path_to_first_file,
        path_to_second_file,
    )