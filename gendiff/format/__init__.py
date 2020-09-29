# -*- coding:utf-8 -*-

"""Init package."""
import json

from gendiff.format import default, plain
from gendiff.format.mapping import mapping_default, mapping_plain


def _compose(g, f):  # noqa: WPS111
    def inner(arg):  # noqa: WPS430
        return g(f(arg))
    return inner


default = _compose(default.format_, mapping_default)
plain = _compose(plain.format_, mapping_plain)
json = _compose(json.dumps, mapping_default)

FORMATTERS = (JSON, PLAIN, DEFAULT) = (  # noqa: WPS429
    'json', 'plain', 'default',
)
