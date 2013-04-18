# FixApply
apply(hello, args, kwargs)

# FixBasestring
basestring

# FixBuffer
buffer('hello', 1, 3)

# FixCallable
callable('hello')

# FixDict
d.keys()
d.iteritems()
d.viewvalues()

# FixExcept
try:
    import asdf
except E, T:
    pass

# FixExec
exec code in ns1, ns2

# FixExecfile
execfile('test.py')

# FixFilter
filter(lambda x: x, [1, 2, 3])

# FixFuncattrs
def test():
    pass
test.func_name
test.func_closure
test.func_dict

# FixFuture
from __future__ import absolute_import

# FixHasKey
d.has_key('foobar')

# FixImport
from py3kwarn import tests

# FixImports
import StringIO
import cStringIO
import cPickle
import __builtin__

# FixInput
input('FixInput')

# FixIntern
intern(s)

# FixIsinstance
isinstance(x, (int, long))
isinstance(x, (int, int))

# FixItertoolsImports
from itertools import imap
from itertools import ifilter
from itertools import izip
from itertools import ifilterfalse

# FixUnicode
u'Hello World'

# FixLong
long

# More...
