# -*- coding:utf-8 -*-

"""Interface for working with a pair of files."""

from gendiff.reader import get_data_from_file


def make_files(path_to_before_file, path_to_after_file):  # noqa: WPS210
    """Create a pair of input files.

    Args:
        path_to_before_file: {tuple(str, str)}.
        path_to_after_file: {tuple(str, str)}.

    Returns:
        dict.
    """
    before_file = get_data_from_file(path_to_before_file)
    after_file = get_data_from_file(path_to_after_file)
    return {
        'before_file': before_file,
        'after_file': after_file,
    }


def get_before_data(files):
    """Return data from the first file.

    Args:
        files: Dictionary pair.

    Returns:
        dict.
    """
    return files['before_file']


def get_after_data(files):
    """Return data from the first file.

    Args:
        files: Dictionary pair.

    Returns:
        dict.
    """
    return files['after_file']
