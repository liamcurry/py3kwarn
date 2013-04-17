==================
py3kwarn |travis|_
==================

py3kwarn is a small wrapper around lib2to3 to help write Python3 compatible
code. It provides flake8-style warning messages.

See the lib2to3_ documentation for information on warning messages.

*Pull requests are welcome!*

Installation
------------

**Requires Python 2.7+**

::

   $ pip install py3kwarn

...or to install from the git repository::

   $ pip install -e git+git://github.com/liamcurry/py3kwarn.git#egg=py3kwarn

Usage from the command line
---------------------------

::

   $ py3kwarn [filename]

Usage with vim
--------------

You can use py3kwarn `with syntastic`_. If you want to use py3kwarn with
another syntax checker (like flake8), then you will have to add this to your
vim config::

   let g:syntastic_python_checkers=['flake8', 'py3kwarn']

TODO
----

- Friendlier messages.
- `A flake8 extension`_.
- Use argparse to add smarter options.
- Make it work with Python 2.6
- Flags to ignore certain errors
- Compatibility mode, where warning messages provide suggestions to write
  forwards compatible code. Make this the default.
- Make it faster. Right now it is quite slow compared to other syntax checkers.
  Major refactoring may be necessary.
- `tox support`_


.. _with syntastic: https://github.com/scrooloose/syntastic/blob/master/syntax_checkers/python/py3kwarn.vim
.. _A flake8 extension: http://flake8.readthedocs.org/en/latest/extensions.html
.. _lib2to3: http://docs.python.org/2.6/library/2to3.html#fixers
.. |travis| image:: https://travis-ci.org/liamcurry/py3kwarn.png
.. _travis: https://travis-ci.org/liamcurry/py3kwarn
.. _tox support: http://tox.readthedocs.org/en/latest/
