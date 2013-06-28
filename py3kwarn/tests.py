# coding=utf-8

from __future__ import unicode_literals

import os
import unittest

from py3kwarn import main


code_apply = 'apply(hello, args, kwargs)'
code_basestring = 'basestring'
code_buffer = "buffer('hello', 1, 3)"
code_callable = "callable('hello')"
code_dict = """
d.keys()
d.iteritems()
d.viewvalues()
"""
code_except = """
try:
    import asdf
except E, T:
    pass
"""
code_exec = 'exec code in ns1, ns2'
code_execfile = "execfile('test.py')"
code_filter = 'filter(lambda x: x, [1, 2, 3])'
code_funcattrs = """
def test():
    pass
test.func_name
test.func_closure
test.func_dict
"""
code_has_key = "d.has_key('foobar')"

code_unicode = "ur'Hello World'"


class TestPy3kWarn(unittest.TestCase):

    def _test_code(self, name, casename=None):
        warnings = main.warnings_for_string(globals()['code_' + name], name)

        if not casename:
            casename = 'Fix' + name.title()

        self.assertTrue(len(warnings))

        self.assertTrue(casename in warnings[0][1])

        return warnings

    def test_apply(self):
        self._test_code('apply')

    def test_basestring(self):
        self._test_code('basestring')

    def test_buffer(self):
        self._test_code('basestring')

    def test_callable(self):
        self._test_code('callable')

    def test_dict(self):
        self._test_code('dict')

    def test_except(self):
        self._test_code('except')

    def test_exec(self):
        self._test_code('exec')

    def test_execfile(self):
        self._test_code('execfile')

    def test_filter(self):
        self._test_code('filter')

    def test_funcattrs(self):
        self._test_code('funcattrs')

    def test_has_key(self):
        self._test_code('has_key', 'HasKey')

    def test_unicode(self):
        self._test_code('unicode')

    def test_do_not_crash_on_unicode(self):
        main.warnings_for_string('u"å"')

    def test_main(self):
        main.main([os.path.join(os.path.dirname(__file__),
                                '__init__.py')])

    def test_with_nonexistent_file(self):
        main.main(['nonexistent_file.py'])

    def test_ignore_compatible_unicode(self):
        self.assertFalse(
            main.warnings_for_string('unicode = str\nunicode("abc")\n'))

    def test_unichr(self):
        self.assertTrue(
            main.warnings_for_string('unichr(1)\n'))

    def test_ignore_compatible_unichr(self):
        self.assertFalse(
            main.warnings_for_string('unichr = chr\nunichr(1)\n'))

    def test_ignore_compatible_basestring(self):
        self.assertFalse(
            main.warnings_for_string('basestring = str\nbasestring\n'))

    def test_xrange(self):
        self.assertTrue(
            main.warnings_for_string('xrange(3)\n'))

    def test_print(self):
        self.assertTrue(
            main.warnings_for_string('print 3\n'))

    def test_print_with_parentheses(self):
        self.assertFalse(
            main.warnings_for_string('print("%d" % 3)\n'))

    def test_imports(self):
        self.assertTrue(
            main.warnings_for_string(
                """\
from ConfigParser import RawConfigParser
"""))

    def test_imports_with_import_error_caught(self):
        self.assertFalse(
            main.warnings_for_string(
                """\
try:
    from ConfigParser import RawConfigParser
except ImportError:
    from configparser import RawConfigParser
"""))

    def test_imports_with_import_error_caught_the_other_way(self):
        self.assertFalse(
            main.warnings_for_string(
                """\
try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser
"""))

    def test_long(self):
        self.assertTrue(
            main.warnings_for_string('long\n'))

    def test_ignore_compatible_long(self):
        self.assertFalse(
            main.warnings_for_string('long = int\nlong\n'))

    def test_zip(self):
        self.assertTrue(
            main.warnings_for_string('zip([1, 2], [3, 4])\n'))

    def test_ignore_compatible_zip(self):
        self.assertFalse(
            main.warnings_for_string('enumerate(zip([1, 2], [3, 4]))\n'))

    def test_raw_input(self):
        self.assertTrue(
            main.warnings_for_string('raw_input()\n'))

    def test_ignore_compatible_raw_input(self):
        self.assertFalse(
            main.warnings_for_string('raw_input = input\nraw_input()\n'))
