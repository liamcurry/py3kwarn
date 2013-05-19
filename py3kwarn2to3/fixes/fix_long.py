# Copyright 2006 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer that turns 'long' into 'int' everywhere.
"""

# Local imports
from py3kwarn2to3 import fixer_base
from py3kwarn2to3.fixer_util import find_binding, is_probably_builtin


class FixLong(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "'long'"

    def start_tree(self, tree, filename):
        super(FixLong, self).start_tree(tree, filename)
        self.skip = find_binding('long', tree)

    def transform(self, node, results):
        if self.skip:
            return

        if is_probably_builtin(node):
            node.value = u"int"
            node.changed()
