# -*- coding:utf-8 -*-

"""Test for building AST."""

from gendiff.nodes import mkast, mknode
from gendiff.parsers.parser import get_data_from_file
from gendiff import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGEABLE,
)


def test_flat_mkast():
    """Flat file testing."""
    filename1 = './tests/fixtures/file1.json'
    filename2 = './tests/fixtures/file2.json'
    actuall = mkast(
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
    assert expectation == actuall  # noqa: S101
