# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lbpackages',
 'lbpackages.create_tables',
 'lbpackages.exceptions',
 'lbpackages.get_data',
 'lbpackages.models',
 'lbpackages.upload_data']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy==1.4.24',
 'pandas>=1.3.4,<2.0.0',
 'psycopg2-binary>=2.9.1,<3.0.0',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'lbpackages',
    'version': '0.2.6',
    'description': 'Implements classes and functions for stocks model and db client',
    'long_description': None,
    'author': 'Lionel Barbagallo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
