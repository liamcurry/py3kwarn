========
py3kwarn
========

.. image:: https://travis-ci.org/liamcurry/py3kwarn.png?branch=master
    :target: https://travis-ci.org/liamcurry/py3kwarn
    :alt: Build status

.. image:: https://coveralls.io/repos/liamcurry/py3kwarn/badge.png?branch=master
    :target: https://coveralls.io/r/liamcurry/py3kwarn
    :alt: Test coverage status

py3kwarn detects code that is not Python 3 compatible. It provides
flake8-style warning messages.

See also:

- The lib2to3_ documentation for information on warning messages.
- `What's new in Python 3.0`_

*Pull requests are welcome!*

Installation
------------

**Supports Python 2.6, 2.7, and 3.3+**

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
    example.py:15:1: PY3K (FixDict) d.iteritems(); -> iter(d.items());
    example.py:16:1: PY3K (FixDict) d.viewvalues(); -> d.values();
    example.py:19:1: PY3K (FixExcept) try:import asdf;except E, T:pass; -> try:import asdf;except E as T:pass;
    example.py:25:1: PY3K (FixExec) exec code in ns1, ns2; -> exec(code, ns1, ns2);
    example.py:28:1: PY3K (FixExecfile) execfile('test.py') -> exec(compile(open('test.py').read(), 'test.py', 'exec'))
    example.py:31:1: PY3K (FixFilter) filter(lambda x: x, [1, 2, 3]) -> [x for x in [1, 2, 3] if x]
    example.py:36:1: PY3K (FixFuncattrs) test.func_name; -> test.__name__;
    example.py:37:1: PY3K (FixFuncattrs) test.func_closure; -> test.__closure__;
    example.py:38:1: PY3K (FixFuncattrs) test.func_dict; -> test.__dict__;
    example.py:44:1: PY3K (FixHasKey) d.has_key('foobar') -> 'foobar' in d
    example.py:56:1: PY3K (FixInput) input('FixInput') -> eval(input('FixInput'))
    example.py:66:1: PY3K (FixItertoolsImports) from itertools import imap -> 
    example.py:67:1: PY3K (FixItertoolsImports) from itertools import ifilter; -> 
    example.py:68:1: PY3K (FixItertoolsImports) from itertools import izip; -> 
    example.py:69:1: PY3K (FixItertoolsImports) from itertools import ifilterfalse; -> from itertools import filterfalse;
    example.py:62:1: PY3K (FixLong) long; -> int;
    example.py:75:1: PY3K (FixLong) long -> int
    example.py:50:1: PY3K (FixImports) import StringIO -> import io
    example.py:51:1: PY3K (FixImports) import cStringIO; -> import io;
    example.py:52:1: PY3K (FixImports) import cPickle; -> import pickle;
    example.py:53:1: PY3K (FixImports) import __builtin__; -> import builtins;
    example.py:62:1: PY3K (FixIsinstance) isinstance(x, (int, int)) -> isinstance(x, int)
    example.py:63:1: PY3K (FixIsinstance) isinstance(x, (int, int)); -> isinstance(x, int);
    example.py:11:1: PY3K (FixCallable) callable('hello') -> isinstance('hello', collections.Callable)
    example.py:59:1: PY3K (FixIntern) intern(s) -> sys.intern(s)

Modifying code automatically
----------------------------

Problems can be fixed via ``py3kwarn2to3``::

    $ py3kwarn2to3 --write example.py

Testing
-------

Testing can be done with ``make test``. py3kwarn also supports `tox`_. This
enables quickly testing changes in many versions of python. Take a look at the
``tox.ini`` file for more details.

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
- Flags to ignore certain errors
- Make it faster. Right now it is quite slow compared to other syntax checkers.
  Major refactoring may be necessary.


.. _What's new in Python 3.0: http://docs.python.org/3/whatsnew/3.0.html
.. _with syntastic: https://github.com/scrooloose/syntastic/blob/master/syntax_checkers/python/py3kwarn.vim
.. _A flake8 extension: http://flake8.readthedocs.org/en/latest/extensions.html
.. _lib2to3: http://docs.python.org/2.6/library/2to3.html#fixers
.. _tox: http://tox.readthedocs.org/en/latest/
