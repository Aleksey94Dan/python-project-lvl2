# -*- coding:utf-8 -*-

"""Expected data for building AST and mapping."""

from operator import itemgetter

from gendiff import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    ROOT,
    UNCHANGEABLE,
)
from gendiff.nodes import get_children, mknode

EXPECTATION_FOR_FLAT_MAPPING_DEFAULT = {  # noqa: WPS407
    '  - follow': False,
    '    host': 'hexlet.io',
    '  - proxy': '123.234.53.22',
    '  - timeout': 50,
    '  + timeout': 20,
    '  + verbose': True,
}

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

EXPECTATION_FOR_FLAT_MAPPING_PLAIN = (
    ('follow', False, DELETED),
    ('proxy', '123.234.53.22', DELETED),
    ('verbose', True, ADDED),
    ('timeout', {OLD_VALUE: 50, NEW_VALUE: 20}, CHANGEABLE),
)


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

EXPECTATION_FLAT_AST = mknode(
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

EXPECTATION_FLAT_AST[CHILDREN].sort(
    key=itemgetter(NAME),
    reverse=False,
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
        children.sort(
            key=itemgetter(NAME),
            reverse=False,
        )
    else:
        return
    for child in children:
        _sorted(child)


_sorted(EXPECTATION_NESTED_AST)


EXPECTATION_FLAT_DEFAULT = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  + timeout: 20
  - timeout: 50
  + verbose: true
}
"""


EXPECTATION_NESTED_DEFAULT = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        fee: 100500
        deep: {
            id: {
                number: 45
            }
        }
    }
}
"""

EXPECTATION_PLAIN = """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to [complex value]
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""

EXPECTATION_JSON = """
{"    common": {"  + follow": false, "    setting1": "Value 1", "  - setting2": 200, "  + setting3": {"key": "value"}, "  - setting3": true, "  + setting4": "blah blah", "  + setting5": {"key5": "value5"}, "    setting6": {"    doge": {"  + wow": "so much", "  - wow": "too much"}, "    key": "value", "  + ops": "vops"}}, "    group1": {"  + baz": "bars", "  - baz": "bas", "    foo": "bar", "  + nest": "str", "  - nest": {"key": "value"}}, "  - group2": {"abc": 12345, "deep": {"id": 45}}, "  + group3": {"fee": 100500, "deep": {"id": {"number": 45}}}}
"""