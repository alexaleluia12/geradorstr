import os
import re
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as readme:
    README = readme.read().decode('utf-8')

# allow setup.py to be run from any path

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('geradorstr/geradorstr.py').read(),
    re.M
    ).group(1)

setup(
    name='geradorstr',
    version=version,
    packages=['geradorstr'],
    entry_points = {
        "console_scripts": ['geradorstr = geradorstr.geradorstr:main']
        },
    license='MIT',
    description='Generate smarts string',
    long_description=README,
    url='https://github.com/alexaleluia12/geradorstr',
    author='Alex Aleluia',
    author_email='alexaleluiaforgit@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: Portuguese (Brazilian)',
        'Topic :: Software Development :: Build Tools',
    ],
)
