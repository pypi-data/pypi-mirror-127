# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slurmer']

package_data = \
{'': ['*']}

install_requires = \
['tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'slurmer',
    'version': '1.0.0',
    'description': 'A package to schedule different tasks in parallel with cluster support.',
    'long_description': None,
    'author': 'Joan Marcè i Igual',
    'author_email': 'J.Marce.i.Igual@tue.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
