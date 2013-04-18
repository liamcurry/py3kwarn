#! /usr/bin/env python
# coding=utf-8

from __future__ import with_statement
from setuptools import setup

APP_NAME = 'py3kwarn'

with open('py3kwarn/__init__.py') as f:
    VERSION = f.readline().split('=')[1]


setup(name=APP_NAME,
      version=VERSION,
      description='A small wrapper around lib2to3 to help write Python 3 compatible code.',
      author='Liam Curry',
      author_email='liam@curry.name',
      url='https://github.com/liamcurry/py3kwarn',
      license='MIT',
      packages=[
          'py3kwarn',
          'py3kwarn2to3', 'py3kwarn2to3.fixes', 'py3kwarn2to3.pgen2'
      ],
      scripts=['py3kwarn/py3kwarn'],
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
