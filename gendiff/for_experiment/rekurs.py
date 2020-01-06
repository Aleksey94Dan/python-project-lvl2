after = {
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


before = {
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


a = {1: 2, 3: 4}
b = {5:5, 3: 4}

deleted = 'DELETED'
added = 'ADDED'
unchangeable = 'UNCHANGEABLE'

def AST_builder(before_data, after_data, key):
    after_value = after_data.setdefault(key, None)
    before_value = before_data.setdefault(key, None)
    if after_value is None:
        node = {
        'type': deleted,
        'key': key,
        'value':  before_data,
      }
    return node

def main():
  common_keys = list(after.keys() | before.keys())
  for common_key in common_keys:
    print(AST_builder(after, before, common_key))


if __name__ == "__main__":
    main()