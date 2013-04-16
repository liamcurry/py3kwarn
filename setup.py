#!/usr/bin/env python
import sys
from py3kwarn import __version__


with open('README.md') as f:
    long_description = f.read()


if sys.version_info[0] == 3:
    from distutils.core import setup
else:
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup


setup(name='py3kwarn',
      license='MIT',
      version=__version__,
      description=('A small wrapper around lib2to3 that provide warnings '
                   'messages for Python 3 incompatible code.'),
      author='Liam Curry',
      author_email='liam@curry.name',
      url='https://github.com/liamcurry/py3kwarn',
      packages=['py3kwarn'],
      scripts=['py3kwarn/py3kwarn'],
      long_description=long_description,
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ])
