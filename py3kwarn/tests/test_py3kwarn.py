from unittest import TestCase


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


class TestPy3kWarn(TestCase):

    def test_apply(self):
        pass

    def test_basestring(self):
        pass

    def test_buffer(self):
        pass

    def test_callable(self):
        pass

    def test_dict(self):
        pass

    def test_except(self):
        pass

    def test_exec(self):
        pass

    def test_execfile(self):
        pass

    def test_filter(self):
        pass

    def test_funcattrs(self):
        pass
