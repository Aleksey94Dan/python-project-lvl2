# -*- coding:utf-8 -*-

"""Constants for testing."""

FLAT_GENDIFF = {
    '  host': 'hexlet.io',
    '+ timeout': 20,
    '- timeout': 50,
    '- proxy': '123.234.53.22',
    '+ verbose': 'true',
}


INSERTED_GENDIFF = {
    '  common': {
        '  setting1': 'Value 1',
        '- setting2': '200',
        '  setting3': 'true',
        '- setting6': {
            'key': 'value',
        },
        '+ setting4': 'blah blah',
        '+ setting5': {
            'key5': 'value5',
        },
    },
    '  group1': {
        '+ baz': 'bars',
        '- baz': 'bas',
        '  foo': 'bar',
    },
    '- group2': {
        'abc': '12345',
    },
    '+ group3': {
        'fee': '100500',
    },
}
