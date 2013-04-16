#!/usr/bin/env python
from py3kwarn import __version__


with open('README.rst') as f:
    long_description = f.read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='py3kwarn',
      version=__version__,
      description=('A small wrapper around lib2to3 to help write Python 3 '
                   'compatible code.'),
      author='Liam Curry',
      author_email='liam@curry.name',
      url='https://github.com/liamcurry/py3kwarn',
      license='MIT',
      packages=['py3kwarn'],
      include_package_data=True,
      package_data={
          '': ['README.rst']
      },
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
