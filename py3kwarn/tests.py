#!/usr/bin/env python
import unittest
from py3kwarn.run import warnings_for_string


code_apply = "apply(hello, args, kwargs)"
code_basestring = "basestring"
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
code_exec = "exec code in ns1, ns2"
code_execfile = "execfile('test.py')"
code_filter = "filter(lambda x: x, [1, 2, 3])"
code_funcattrs = """
def test():
    pass
test.func_name
test.func_closure
test.func_dict
"""
code_future = "from __future__ import absolute_import"
code_has_key = "d.has_key('foobar')"
code_imports = """
import StringIO
import dbm
"""
code_unicode = "u'Hello World'"


class TestPy3kWarn(unittest.TestCase):

    def _test_code(self, name, casename=None):
        warnings = warnings_for_string(globals()['code_' + name], name)
        if not casename:
            casename = 'Fix' + name.title()
        self.assertTrue(len(warnings))
        self.assertIn(casename, warnings[0][1])
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
        #self._test_code('funcattrs')
        pass

    def test_future(self):
        self._test_code('future')

    def test_has_key(self):
        self._test_code('has_key', 'HasKey')

    def test_imports(self):
        #self._test_code('imports')
        pass

    def test_unicode(self):
        self._test_code('unicode')



if __name__ == '__main__':
    unittest.main()
