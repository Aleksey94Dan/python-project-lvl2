import pytest
from gendiff.generate_diff import generate_diff


def test_gendiff():
    with open('/home/all_done/Hexlet/projects/python-project-lvl2/gendiff/tests/fixtures/diff.txt') as diff_file:
        a = diff_file.read()
    b = generate_diff('gendiff/tests/fixtures/after.json',
    'gendiff/tests/fixtures/before.json')
    assert a == b

