"""Fixer that changes raw_input(...) into input(...)."""
# Author: Andre Roberge

from .. import fixer_base
from ..fixer_util import Name
from ..fixer_util import find_binding

class FixRawInput(fixer_base.BaseFix):

    BM_compatible = True
    PATTERN = """
              power< name='raw_input' trailer< '(' [any] ')' > any* >
              """

    def start_tree(self, tree, filename):
        super(FixRawInput, self).start_tree(tree, filename)
        self.skip = find_binding('raw_input', tree)

    def transform(self, node, results):
        if self.skip:
            return

        name = results["name"]
        name.replace(Name(u"input", prefix=name.prefix))
