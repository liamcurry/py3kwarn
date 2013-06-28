"""Fixer that changes unicode to str, unichr to chr, and u"..." into "...".

"""

import re

from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import find_binding

_mapping = {u"unichr" : u"chr", u"unicode" : u"str"}
_literal_re = re.compile(r"[uU][rR][\'\"]")

class FixUnicode(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "STRING | 'unicode' | 'unichr'"

    def start_tree(self, tree, filename):
        super(FixUnicode, self).start_tree(tree, filename)
        self.skip = (find_binding('unicode', tree) or
                     find_binding('unichr', tree))

    def transform(self, node, results):
        if self.skip:
            return

        if node.type == token.NAME:
            new = node.clone()
            new.value = _mapping[node.value]
            return new
        elif node.type == token.STRING:
            if _literal_re.match(node.value):
                new = node.clone()
                new.value = new.value[1:]
                return new
