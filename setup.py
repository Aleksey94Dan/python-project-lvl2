# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gendiff', 'gendiff.format', 'gendiff.scripts']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.8.3,<4.0.0', 'isort==4.3.21']

entry_points = \
{'console_scripts': ['gendiff = gendiff.scripts.gendiff:main']}

setup_kwargs = {
    'name': 'aleksey94dan-gendiff',
    'version': '0.11.0',
    'description': 'This utility looks for differences in configuration files.',
    'long_description': None,
    'author': 'Aleksey Danilchenko',
    'author_email': 'danilchenko.aleksey94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
