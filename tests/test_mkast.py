# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff.nodes import mknode, mkast
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


def test_flat_mkast():
    """Flat file testing."""
    filename1 = './tests/fixtures/flat_file/file1.json'
    filename2 = './tests/fixtures/flat_file/file2.json'

    actuall_json = mkast(
        get_data_from_file(filename1),
        get_data_from_file(filename2),
    )

    filename1 = './tests/fixtures/flat_file/file1.yml'
    filename2 = './tests/fixtures/flat_file/file2.yml'

    actuall_yml = mkast(
        get_data_from_file(filename1),
        get_data_from_file(filename2),
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
    assert expectation == mknode(
        name=ROOT,
        children=actuall_json,
    )
    assert expectation == mknode(
        name=ROOT,
        children=actuall_yml,
    )
