# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff.nodes import mknode, mkast, get_children
from gendiff.parsers import get_data_from_file
from gendiff import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGEABLE,
    ROOT,
)


def sorted_(node):
    """Sorted nested structure."""
    children = get_children(node)
    if children:
        children.sort(
            key=lambda name_of_key: name_of_key[NAME],
            reverse=False,
        )
    else:
        return
    for child in children:
        sorted_(child)


def test_flat_mkast():
    """Flat file testing."""
    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'

    actual_json = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    filename1 = './tests/fixtures/flat_files/file1.yml'
    filename2 = './tests/fixtures/flat_files/file2.yml'

    actual_yml = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    expectation = mknode(
        name='root',
        children=[
            mknode(
                name='host',
                status=UNCHANGEABLE,
                value='hexlet.io',
            ),
            mknode(
                name='timeout',
                status=CHANGEABLE,
                value={OLD_VALUE: 50, NEW_VALUE: 20},
            ),
            mknode(
                name='proxy',
                status=DELETED,
                value='123.234.53.22',
            ),
            mknode(
                name='follow',
                status=DELETED,
                value=False,
            ),
            mknode(
                name='verbose',
                status=ADDED,
                value=True,
            ),
        ],
    )
    expectation[CHILDREN].sort(
        key=lambda name_of_key: name_of_key[NAME],
        reverse=False,
    )
    assert expectation == actual_json  # noqa: S101
    assert expectation == actual_yml  # noqa: S101


def test_nested_mkast():
    """Nested file testing."""
    filename1 = './tests/fixtures/nested_files/file1.json'
    filename2 = './tests/fixtures/nested_files/file2.json'

    actual_json = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    filename1 = './tests/fixtures/nested_files/file1.yml'
    filename2 = './tests/fixtures/nested_files/file2.yml'

    actual_yml = mknode(
        name=ROOT,
        children=mkast(
            get_data_from_file(filename1),
            get_data_from_file(filename2),
        ),
    )

    expectation = mknode(
        name=ROOT,
        children=[
            mknode(
                name='common',
                children=[
                    mknode(
                        name='follow',
                        status=ADDED,
                        value=False,
                    ),
                    mknode(
                        name='setting1',
                        status=UNCHANGEABLE,
                        value='Value 1',
                    ),
                    mknode(
                        name='setting2',
                        status=DELETED,
                        value=200,  # noqa: WPS432
                    ),
                    mknode(
                        name='setting3',
                        status=CHANGEABLE,
                        value={OLD_VALUE: True, NEW_VALUE: {'key': 'value'}},
                    ),
                    mknode(
                        name='setting4',
                        status=ADDED,
                        value='blah blah',
                    ),
                    mknode(
                        name='setting5',
                        status=ADDED,
                        value={'key5': 'value5'},
                    ),
                    mknode(
                        name='setting6',
                        children=[
                            mknode(
                                name='doge',
                                children=[
                                    mknode(
                                        name='wow',
                                        status=CHANGEABLE,
                                        value={
                                            OLD_VALUE: 'too much',
                                            NEW_VALUE: 'so much',
                                        },
                                    ),
                                ],
                            ),
                            mknode(
                                name='key',
                                status=UNCHANGEABLE,
                                value='value',
                            ),
                            mknode(
                                name='ops',
                                status=ADDED,
                                value='vops',
                            ),
                        ],
                    ),
                ],
            ),
            mknode(
                name='group1',
                children=[
                    mknode(
                        name='baz',
                        status=CHANGEABLE,
                        value={OLD_VALUE: 'bas', NEW_VALUE: 'bars'},
                    ),
                    mknode(
                        name='foo',
                        status=UNCHANGEABLE,
                        value='bar',
                    ),
                    mknode(
                        name='nest',
                        status=CHANGEABLE,
                        value={OLD_VALUE: {'key': 'value'}, NEW_VALUE: 'str'},
                    ),
                ],
            ),
            mknode(
                name='group2',
                status=DELETED,
                value={
                    'abc': 12345,
                    'deep': {
                        'id': 45,
                    },
                },
            ),
            mknode(
                name='group3',
                status=ADDED,
                value={
                    'fee': 100500,
                    'deep': {
                        'id': {
                            'number': 45,
                        },
                    },
                },
            ),
        ],
    )

    sorted_(expectation)
    assert expectation == actual_json  # noqa: S101
    assert expectation == actual_yml  # noqa: S101
