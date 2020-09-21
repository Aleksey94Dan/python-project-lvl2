# -*- coding:utf-8 -*-

"""Test for format."""
from gendiff.nodes import mknode, mkast
from gendiff.format.mapping import get_mapping
from gendiff.parsers import get_data_from_file
from gendiff import ROOT


def test_mapping_format_defatult():  # noqa: WPS210
    """Test mapping for flat and nested files."""
    expectation_for_flat = {
        '  - follow': False,
        '    host': 'hexlet.io',
        '  - proxy': '123.234.53.22',
        '  - timeout': 50,
        '  + timeout': 20,
        '  + verbose': True,
    }

    expectation_for_nested = {
        '    common': {
            '  + follow': False,
            '    setting1': 'Value 1',
            '  - setting2': 200,
            '  - setting3': True,
            '  + setting3': {
                'key': 'value',
            },
            '  + setting4': 'blah blah',
            '  + setting5': {
                'key5': 'value5',
            },
            '    setting6': {
                '    doge': {
                    '  + wow': 'so much',
                    '  - wow': 'too much',
                },
                '    key': 'value',
                '  + ops': 'vops',
            },
        },
        '    group1': {
            '    foo': 'bar',
            '  - baz': 'bas',
            '  + baz': 'bars',
            '  - nest': {
                'key': 'value',
            },
            '  + nest': 'str',
        },
        '  - group2': {
            'abc': 12345,
            'deep': {
                'id': 45,
            },
        },
        '  + group3': {
            'deep': {
                'id': {
                    'number': 45,
                },
            },
            'fee': 100500,
        },
    }

    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'

    actual_flat = get_mapping(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )

    filename1 = './tests/fixtures/nested_files/file1.json'
    filename2 = './tests/fixtures/nested_files/file2.json'

    actual_nested = get_mapping(
        mknode(
            name=ROOT,
            children=mkast(
                get_data_from_file(filename1),
                get_data_from_file(filename2),
            ),
        ),
    )

    assert expectation_for_flat == actual_flat  # noqa: S101
    assert expectation_for_nested == actual_nested  # noqa: S101
