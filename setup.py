from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='c2singlefile',
    version='0.1',
    packages=['c2singlefile'],
    url='https://github.com/Depaulicious/c2singlefile',
    license='GPLv3',
    author='Davide Depau',
    author_email='davide@depau.eu',
    description='Turns a bunch of specially formatted c files into a single file',
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "c2singlefile = c2singlefile:main",
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='c parser'
)
