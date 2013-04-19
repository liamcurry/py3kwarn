#! /usr/bin/env python
# coding=utf-8

from __future__ import with_statement

import ast
import sys

from setuptools import setup


if sys.version_info >= (3, 0):
    raise SystemExit("py3kwarn requires Python 2.6 or 2.7")

APP_NAME = 'py3kwarn'

with open('py3kwarn/__init__.py') as f:
    for line in f:
        if line.startswith('__version__'):
            VERSION = ast.parse(line).body[0].value.s


setup(name=APP_NAME,
      version=VERSION,
      description='A small wrapper around lib2to3 to help write Python 3 '
                  'compatible code.',
      author='Liam Curry',
      author_email='liam@curry.name',
      url='https://github.com/liamcurry/py3kwarn',
      license='MIT',
      packages=[
          'py3kwarn',
          'py3kwarn2to3', 'py3kwarn2to3.fixes', 'py3kwarn2to3.pgen2'
      ],
      package_data={'py3kwarn2to3': ['*.txt']},
      zip_safe=False,
      entry_points={'console_scripts': ['py3kwarn=py3kwarn.run:main']},
      long_description=open('README.rst').read(),
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ],
      test_suite='py3kwarn.tests')
