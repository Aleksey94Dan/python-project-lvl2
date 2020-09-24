# -*- coding:utf-8 -*-

"""Format plain."""

from gendiff.nodes import get_children, get_name, get_value, get_status

TEMPLATE_FOR_DELETED = "Property {} was removed"
TEMPLATE_FOR_ADDED = "Property '{}' was added with value: {}"
TEMPLATE_FOR_CHANGEABLE = "Property {} was updated. From '{}' to '{}'"

source = {'children': [{'children': [{'children': None,
                             'name': 'follow',
                             'status': 'added',
                             'value': False},
                            {'children': None,
                             'name': 'setting1',
                             'status': 'unchangeable',
                             'value': 'Value 1'},
                            {'children': None,
                             'name': 'setting2',
                             'status': 'deleted',
                             'value': 200},
                            {'children': None,
                             'name': 'setting3',
                             'status': 'changeable',
                             'value': {'new_value': {'key': 'value'},
                                       'old_value': True}},
                            {'children': None,
                             'name': 'setting4',
                             'status': 'added',
                             'value': 'blah blah'},
                            {'children': None,
                             'name': 'setting5',
                             'status': 'added',
                             'value': {'key5': 'value5'}},
                            {'children': [{'children': [{'children': None,
                                                         'name': 'wow',
                                                         'status': 'changeable',
                                                         'value': {'new_value': 'so '
                                                                                'much',
                                                                   'old_value': 'too '
                                                                                'much'}}],
                                           'name': 'doge',
                                           'status': None,
                                           'value': None},
                                          {'children': None,
                                           'name': 'key',
                                           'status': 'unchangeable',
                                           'value': 'value'},
                                          {'children': None,
                                           'name': 'ops',
                                           'status': 'added',
                                           'value': 'vops'}],
                             'name': 'setting6',
                             'status': None,
                             'value': None}],
               'name': 'common',
               'status': None,
               'value': None},
              {'children': [{'children': None,
                             'name': 'baz',
                             'status': 'changeable',
                             'value': {'new_value': 'bars',
                                       'old_value': 'bas'}},
                            {'children': None,
                             'name': 'foo',
                             'status': 'unchangeable',
                             'value': 'bar'},
                            {'children': None,
                             'name': 'nest',
                             'status': 'changeable',
                             'value': {'new_value': 'str',
                                       'old_value': {'key': 'value'}}}],
               'name': 'group1',
               'status': None,
               'value': None},
              {'children': None,
               'name': 'group2',
               'status': 'deleted',
               'value': {'abc': 12345, 'deep': {'id': 45}}},
              {'children': None,
               'name': 'group3',
               'status': 'added',
               'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}],
 'name': 'root',
 'status': None,
 'value': None}


def get_mapping(tree):

    acc = []
    def inner(node, path=[]):
        children = get_children(node)
        current_value = get_value(node)

        if not children:
            path.append(current_value)
            return

        for child in children:
            new_path = path.copy()
            name = get_name(child)

            if child:
                if name not in path:
                    new_path.append(name)
                    inner(child, new_path)
            else:
                new_path.append(name)
            acc.append(new_path)
        if path:
            path.pop()
        return acc
    return inner(tree)



if __name__ == "__main__":
    from pprint import pprint
    pprint(get_mapping(source))

