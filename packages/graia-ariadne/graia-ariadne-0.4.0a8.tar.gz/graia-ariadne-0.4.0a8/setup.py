# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['graia',
 'graia.ariadne',
 'graia.ariadne.event',
 'graia.ariadne.message',
 'graia.ariadne.message.parser']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'graia-broadcast>=0.12.1',
 'loguru>=0.5.3,<0.6.0',
 'pydantic>=1.8.2,<2.0.0',
 'typing-extensions>=3.10.0,<4.0.0',
 'yarl>=1.6.3,<2.0.0']

setup_kwargs = {
    'name': 'graia-ariadne',
    'version': '0.4.0a8',
    'description': 'Anelegant mirai-api-http v2 Python SDK.',
    'long_description': None,
    'author': 'BlueGlassBlock',
    'author_email': 'blueglassblock@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
