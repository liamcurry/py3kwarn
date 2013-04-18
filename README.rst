========
py3kwarn
========

.. image:: https://travis-ci.org/liamcurry/py3kwarn.png?branch=master
   :target: https://travis-ci.org/liamcurry/py3kwarn
   :alt: Build status

.. image:: https://coveralls.io/repos/liamcurry/py3kwarn/badge.png?branch=master
   :target: https://coveralls.io/r/liamcurry/py3kwarn
   :alt: Test coverage status

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

    $ py3kwarn example.py
    example.py:2:1: PY3K (FixApply) apply(hello, args, kwargs) -> hello(*args, **kwargs)
    example.py:5:1: PY3K (FixBasestring) basestring -> str
    example.py:11:1: PY3K (FixCallable) callable('hello') -> isinstance('hello', collections.Callable)
    example.py:14:1: PY3K (FixDict) d.keys() -> list(d.keys())
    example.py:15:1: PY3K (FixDict) d.iteritems(); -> iter(d.items());
    example.py:16:1: PY3K (FixDict) d.viewvalues(); -> d.values();
    example.py:19:1: PY3K (FixExcept) try:import asdf;except E, T:pass; -> try:import asdf;except E as T:pass;
    example.py:25:1: PY3K (FixExec) exec code in ns1, ns2; -> exec(code, ns1, ns2);
    example.py:28:1: PY3K (FixExecfile) execfile('test.py') -> exec(compile(open('test.py').read(), 'test.py', 'exec'))
    example.py:31:1: PY3K (FixFilter) filter(lambda x: x, [1, 2, 3]) -> [x for x in [1, 2, 3] if x]
    example.py:41:1: PY3K (FixFuture) from __future__ import absolute_import ->
    example.py:44:1: PY3K (FixHasKey) d.has_key('foobar') -> 'foobar' in d
    example.py:56:1: PY3K (FixInput) input('FixInput') -> eval(input('FixInput'))
    example.py:59:1: PY3K (FixIntern) intern(s) -> sys.intern(s)

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
.. _tox: http://tox.readthedocs.org/en/latest/
.. _pythonbrew: https://github.com/utahta/pythonbrew
