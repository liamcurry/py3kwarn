# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Fixer that changes xrange(...) into range(...)."""

# Local imports
from .. import fixer_base
from ..fixer_util import Name


class FixXrange(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
              power<
                 (name='xrange') trailer< '(' args=any ')' >
              rest=any* >
              """

    def start_tree(self, tree, filename):
        super(FixXrange, self).start_tree(tree, filename)
        self.transformed_xranges = set()

    def finish_tree(self, tree, filename):
        self.transformed_xranges = None

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name(u"range", prefix=name.prefix))
