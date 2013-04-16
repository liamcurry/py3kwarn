# py3kwarn [![Build Status](https://travis-ci.org/liamcurry/py3kwarn.png)][travis]

py3kwarn is a small wrapper around lib2to3 to help write Python3 compatible
code. It provides flake8-style warning messages.

Currently requires Python 2.7+.

See the [lib2to3][lib2to3] documentation for information on warning messages.

*Pull requests are welcome!*

## Install

Install using `pip install py3kwarn`, or to install from the git repository:

```shell
git clone git://github.com/liamcurry/py3kwarn.git
cd py3kwarn
make install
```

## Usage

### From the command line

```shell
py3kwarn test.py
```

### With vim

To use with vim, check out [my syntastic fork][my-fork]
which adds py3kwarn as a syntax checker for python. If you want to use py3kwarn
and syntastic with another syntax checker (like flake8), then you will have to
add this to your vim config:

```vim
let g:syntastic_python_checkers=['flake8', 'py3kwarn']
```

## TODO

- An option for friendlier messages would be nice.
- [A flake8 extension][flake8-ext].
- Use argparse to add some smarter options.
- Better docs
- Make it work with Python 2.6


[my-fork]: https://github.com/liamcurry/syntastic/tree/py3kwarn
[travis]: https://travis-ci.org/liamcurry/py3kwarn
[flake8-ext]: http://flake8.readthedocs.org/en/latest/extensions.html
[lib2to3]: http://docs.python.org/2.6/library/2to3.html#fixers
