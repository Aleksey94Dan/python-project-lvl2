# -*- coding:utf-8 -*-

"""Init package."""
from gendiff.format import default
from gendiff.format import plain
from gendiff.format.mapping import mapping_default, mapping_plain


def _compose(g, f):  # noqa: WPS111
    def inner(arg):  # noqa: WPS430
        return g(f(arg))
    return inner


default = _compose(default.format_, mapping_default)
plain = _compose(plain.format_, mapping_plain)


FORMATTERS = (JSON, PLAIN, DEFAULT) = (  # noqa: WPS429
    'json', 'plain', 'default',
)
