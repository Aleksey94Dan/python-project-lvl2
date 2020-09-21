# -*- coding:utf-8 -*-

"""Test for format."""

from gendiff.nodes import mkast, get_children, mknode
from gendiff.parsers import get_data_from_file
from gendiff import (
    ADDED,
    CHANGEABLE,
    CHILDREN,
    DELETED,
    NAME,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGEABLE,
    ROOT,
)


def test_format_default():
  """Test format default for flat and nested files."""
    filename1 = './tests/fixtures/flat_files/file1.json'
    filename2 = './tests/fixtures/flat_files/file2.json'
    
