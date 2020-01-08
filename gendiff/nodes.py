# -*- coding:utf-8 -*-


"""The module describes the rules for building nodes."""


def AST_builder(before_file, after_file):
    common_keys = list(after_file.keys() | before_file.keys())
    return {key: get_node(before_file, after_file, key) for key in common_keys}



def get_node(before_file, after_file, key):  # noqa: WPS231
    """Return node.

    Args:
        before_file: First file for compare.
        after_file:  Second file for compare.
        key: Keyword for comparison.

    Returns:
        dict.
    """
    before = before_file.get(key)
    after = after_file.get(key)

    if before is None:  # noqa: WPS223
        return {
            'type': 'ADDED',
            'key': key,
            'value': after,
        }
    elif after is None:
        return {
            'type': 'DELETED',
            'key': key,
            'value': before,
        }
    elif isinstance(before, dict) and isinstance(after, dict):
        return {
            'type': 'PARRENT',
            'key': key,
            'child': AST_builder(before, after),
        }
    elif before == after:
        return {
            'type': 'UNCHANGEABLE',
            'key': key,
            'value': after,
        }
    elif before != after:
        return {
            'type': 'CHANGEABLE',
            'key': key,
            'before_value': before,
            'after_value': after,
        }

a = {
    "common": {
      "setting1": "Value 1",
      "setting3": True,
      "setting4": "blah blah",
      "setting5": {
        "key5": "value5"
      }
    },

    "group1": {
      "foo": "bar",
      "baz": "bars"
    },

    "group3": {
      "fee": "100500"
    }
  }

b = {
    "common": {
      "setting1": "Value 1",
      "setting2": "200",
      "setting3": True,
      "setting6": {
        "key": "value"
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar"
    },
    "group2": {
      "abc": "12345"
    }
  }




def main():
    print(AST_builder(a, b))


if __name__ == "__main__":
    main()
