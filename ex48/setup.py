try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Daniel Newman',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dwnewman78@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
