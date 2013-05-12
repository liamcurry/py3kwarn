"""Fixer for basestring -> str."""
# Author: Christian Heimes

# Local imports
from .. import fixer_base
from ..fixer_util import find_binding, Name

class FixBasestring(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = "'basestring'"

    def start_tree(self, tree, filename):
        super(FixBasestring, self).start_tree(tree, filename)
        self.skip = find_binding('basestring', tree)

    def transform(self, node, results):
        if self.skip:
            return

        return Name(u"str", prefix=node.prefix)
