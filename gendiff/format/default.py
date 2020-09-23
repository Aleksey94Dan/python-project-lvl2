def formater(source, indent=0):
    for key, value in source.items():
        if isinstance(value, bool):
            value = str(value).lower()
        if ' ' not in str(key):
            key = '\t' + key
        if isinstance(value, dict):
            print('{}{} {{'.format(indent*sing, key))
            formater(value, indent+1)
            print('{}}}'.format(indent*sing))
        else:
            print('{}{}: {}'.format(sing * indent, str(key), str(value)))
