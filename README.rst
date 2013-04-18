==================
py3kwarn |travis|_
==================

py3kwarn is a small wrapper around lib2to3 to help write Python3 compatible
code. It provides flake8-style warning messages.

See the lib2to3_ documentation for information on warning messages.

*Pull requests are welcome!*

Installation
------------

**Requires Python 2.6 or 2.7+**

::

   $ pip install py3kwarn

...or to install from the git repository::

   $ pip install -e git+git://github.com/liamcurry/py3kwarn.git#egg=py3kwarn

Usage with vim
--------------

You can use py3kwarn `with syntastic`_. If you want to use py3kwarn with
another syntax checker (like flake8), then you will have to add this to your
vim config::

   let g:syntastic_python_checkers=['flake8', 'py3kwarn']

Usage from the command line
---------------------------

::

   $ py3kwarn [filename]

Testing
-------

Testing can be done with ``make test``. py3kwarn also supports `tox`_, which
assumes `pythonbrew`_ is installed. This enables quickly testing changes in
many versions of python. Take a look at the ``tox.ini`` file for more details.

Contributing
------------
To contribute, fork the repo and clone to your local machine.

Create a virtual environment and ::

    pip install -r requirements_dev.txt

Then just make a pull request with the issues you've fixed!

TODO
----

- Friendlier messages.
- `A flake8 extension`_.
- Use argparse to add smarter options.
- Flags to ignore certain errors
- Compatibility mode, where warning messages provide suggestions to write
  forwards compatible code. Make this the default.
- Make it faster. Right now it is quite slow compared to other syntax checkers.
  Major refactoring may be necessary.


.. _with syntastic: https://github.com/scrooloose/syntastic/blob/master/syntax_checkers/python/py3kwarn.vim
.. _A flake8 extension: http://flake8.readthedocs.org/en/latest/extensions.html
.. _lib2to3: http://docs.python.org/2.6/library/2to3.html#fixers
.. |travis| image:: https://travis-ci.org/liamcurry/py3kwarn.png
.. _travis: https://travis-ci.org/liamcurry/py3kwarn
.. _tox: http://tox.readthedocs.org/en/latest/
.. _pythonbrew: https://github.com/utahta/pythonbrew
