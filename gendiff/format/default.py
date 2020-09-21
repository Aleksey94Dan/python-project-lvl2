# -*- coding:utf-8 -*-

"""The template for default formatting."""
from gendiff.nodes import get_children, get_name, get_value, get_status, mknode
from gendiff import (
    UNCHANGEABLE,
    CHANGEABLE,
    ADDED,
    DELETED,
    OLD_VALUE,
    NEW_VALUE,
    ROOT,
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



def get_mapping(tree, name=None, status=None, depth=0):  # noqa: D103, WPS210, WPS231
    children = get_children(tree)
    value = get_value(tree)

    if status is CHANGEABLE:
        return {
            ' + {}'.format(name): value.get(NEW_VALUE),
            ' - {}'.format(name): value.get(OLD_VALUE),
        }

    if not children:
        return value
    acc = {}
    for child in children:
        name = get_name(child)
        status = get_status(child)
        if status is ADDED:
            name = '  {} {}'.format('+', name)
            acc.update({name: get_mapping(child)})
        elif status is DELETED:
            name = '  {} {}'.format('-', name)
            acc.update({name: get_mapping(child)})
        elif status is UNCHANGEABLE:
            name = '    {}'.format(name)
            acc.update({name: get_mapping(child)})
        elif status is None:
            name = '    {}'.format(name)
            acc.update({name: get_mapping(child)})
        elif status is CHANGEABLE:
            acc.update(get_mapping(child, name=name, status=status))
    return acc



if __name__== '__main__':
    from pprint import pprint
    # pprint(expectation)
    pprint(pretty_print(expectation))

