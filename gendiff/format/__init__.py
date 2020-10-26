# -*- coding:utf-8 -*-

"""Init package."""
import json

from gendiff.format import default, plain


def _compose(g, f):  # noqa: WPS111
    def inner(arg):  # noqa: WPS430
        return g(f(arg))
    return inner


default = _compose(default.format, default.mapping)
plain = _compose(plain.format, plain.mapping)
json = json.dumps

FORMATTERS = (JSON, PLAIN, DEFAULT) = (  # noqa: WPS429
    'json', 'plain', 'default',
)
