#!/usr/bin/env python
from setuptools import setup


def get_version(fname='py3kwarn/__init__.py'):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    with open('README.rst') as f:
        return f.read()


setup(name='py3kwarn',
      version=get_version(),
      description=('A small wrapper around lib2to3 to help write Python 3 '
                   'compatible code.'),
      author='Liam Curry',
      author_email='liam@curry.name',
      url='https://github.com/liamcurry/py3kwarn',
      license='MIT',
      packages=['py3kwarn'],
      scripts=['py3kwarn/py3kwarn'],
      long_description=get_long_description(),
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ])
