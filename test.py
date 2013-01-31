# apply
apply(hello, args, kwargs)

# basestring
basestring

# buffer
buffer('hello', 1, 3)

# callable
callable('hello')

# dict
d.keys()
d.iteritems()
d.viewvalues()

# except
try:
    import asdf
except E, T:
    pass

# exec
exec code in ns1, ns2

# execfile
execfile('test.py')

# filter
filter(lambda x: x, [1, 2, 3])

# funcattrs
def test():
    pass
test.func_name
test.func_closure
test.func_dict

# future
from __future__ import absolute_import

# has_key
d.has_key('foobar')

# idioms

# imports
import StringIO
import dbm
