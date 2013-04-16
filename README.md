# py3kwarn [![Build Status](https://travis-ci.org/liamcurry/py3kwarn.png)][travis]

py3kwarn is a small wrapper around lib2to3 to help write Python3 compatible
code. It provides flake8-style warning messages.

*Pull requests are welcome!*

## Usage

`py3kwarn test.py`

## Use with vim

To use with vim, check out [my syntastic fork][my-fork]
which adds py3kwarn as a syntax checker for python. If you want to use py3kwarn
and syntastic with another syntax checker (like flake8), then you will have to
add `let g:syntastic_python_checkers=['flake8', 'py3kwarn']` to your vim
config.

## TODO

* An option for friendlier messages would be nice.
* [A flake8 extension][flake8-ext].
* Use argparse to add some smarter options.
* Better docs


[my-fork]: https://github.com/liamcurry/syntastic/tree/py3kwarn
[travis]: https://travis-ci.org/liamcurry/py3kwarn
[flake8-ext]: http://flake8.readthedocs.org/en/latest/extensions.html
