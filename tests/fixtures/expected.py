# -*- coding:utf-8 -*-

"""Expected data for building AST and mapping."""

from operator import itemgetter

from gendiff import (
    ADDED,
    CHANGEABLE,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    ROOT,
    UNCHANGEABLE,
)
from gendiff.nodes import get_children, mknode

filename_flat1 = 'tests/fixtures/flat_files/file1.yml'
filename_flat2 = 'tests/fixtures/flat_files/file2.json'
filename_nested1 = 'tests/fixtures/nested_files/file1.json'
filename_nested2 = 'tests/fixtures/nested_files/file2.yml'
fake_flat = 'tests/fixtures/flat_files/file1.ymls'
fake_format = 'ini'
cmd_format = '-f'
extension = ('default', 'json', 'plain')
nested_default = 'tests/fixtures/expectation_nested_default.txt'
nested_plain = 'tests/fixtures/expectation_plain.txt'


EXPECTATION_FOR_NESTED_MAPPING_DEFAULT = {  # noqa: WPS407
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


EXPECTATION_FOR_NESTED_MAPPING_PLAIN = (
    ('common.follow', False, ADDED),
    ('common.setting2', 200, DELETED),
    (
        'common.setting3',
        {OLD_VALUE: True, NEW_VALUE: {'key': 'value'}},
        CHANGEABLE,
    ),
    ('common.setting4', 'blah blah', ADDED),
    ('common.setting5', {'key5': 'value5'}, ADDED),
    (
        'common.setting6.doge.wow',
        {OLD_VALUE: 'too much', NEW_VALUE: 'so much'},
        CHANGEABLE,
    ),
    ('common.setting6.ops', 'vops', ADDED),
    ('group1.baz', {OLD_VALUE: 'bas', NEW_VALUE: 'bars'}, CHANGEABLE),
    (
        'group1.nest',
        {OLD_VALUE: {'key': 'value'}, NEW_VALUE: 'str'},
        CHANGEABLE,
    ),
    ('group2', {'abc': 12345, 'deep': {'id': 45}}, DELETED),
    ('group3', {'fee': 100500, 'deep': {'id': {'number': 45}}}, ADDED),
)


EXPECTATION_NESTED_AST = mknode(
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


def _sorted(node):
    """Sorted nested structure."""
    children = get_children(node)
    if children:
        children.sort(key=itemgetter(NAME), reverse=False)
    else:
        return
    for child in children:
        _sorted(child)


_sorted(EXPECTATION_NESTED_AST)

with open(nested_default) as nested:
    EXPECTATION_NESTED_DEFAULT = nested.read()

with open(nested_plain) as plain:
    EXPECTATION_PLAIN = plain.read()
