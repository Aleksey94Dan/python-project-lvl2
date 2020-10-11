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
    CHILDREN
)
from gendiff.nodes import make_node

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


EXPECTATION_NESTED_AST = make_node(
    name=ROOT,
    children=[
        make_node(
            name='common',
            children=[
                make_node(
                    name='follow',
                    status=ADDED,
                    current_value=False,
                ),
                make_node(
                    name='setting1',
                    status=UNCHANGEABLE,
                    current_value='Value 1',
                ),
                make_node(
                    name='setting2',
                    status=DELETED,
                    current_value=200,  # noqa: WPS432
                ),
                make_node(
                    name='setting3',
                    status=CHANGEABLE,
                    current_value={
                        OLD_VALUE: True,
                        NEW_VALUE: {'key': 'value'},
                    },
                ),
                make_node(
                    name='setting4',
                    status=ADDED,
                    current_value='blah blah',
                ),
                make_node(
                    name='setting5',
                    status=ADDED,
                    current_value={'key5': 'value5'},
                ),
                make_node(
                    name='setting6',
                    children=[
                        make_node(
                            name='doge',
                            children=[
                                make_node(
                                    name='wow',
                                    status=CHANGEABLE,
                                    current_value={
                                        OLD_VALUE: 'too much',
                                        NEW_VALUE: 'so much',
                                    },
                                ),
                            ],
                        ),
                        make_node(
                            name='key',
                            status=UNCHANGEABLE,
                            current_value='value',
                        ),
                        make_node(
                            name='ops',
                            status=ADDED,
                            current_value='vops',
                        ),
                    ],
                ),
            ],
        ),
        make_node(
            name='group1',
            children=[
                make_node(
                    name='baz',
                    status=CHANGEABLE,
                    current_value={OLD_VALUE: 'bas', NEW_VALUE: 'bars'},
                ),
                make_node(
                    name='foo',
                    status=UNCHANGEABLE,
                    current_value='bar',
                ),
                make_node(
                    name='nest',
                    status=CHANGEABLE,
                    current_value={
                        OLD_VALUE: {'key': 'value'},
                        NEW_VALUE: 'str',
                    },
                ),
            ],
        ),
        make_node(
            name='group2',
            status=DELETED,
            current_value={
                'abc': 12345,
                'deep': {
                    'id': 45,
                },
            },
        ),
        make_node(
            name='group3',
            status=ADDED,
            current_value={
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
    children = node.get(CHILDREN)
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
