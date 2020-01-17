# -*- coding:utf-8 -*-

"""Interface for working with a pair of files."""


def make_files(before_file, after_file):  # noqa: WPS210
    """Create a pair of input files.

    Args:
        before_file: file before change.
        after_file: file after change.

    Returns:
        dict.
    """
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
