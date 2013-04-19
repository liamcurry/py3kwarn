#! /usr/bin/env python
# coding=utf-8

from itertools import chain
import sys

from . import __version__

from py3kwarn2to3 import refactor, pytree
from py3kwarn2to3.fixer_util import find_root


def to_warn_str(node):
    lines = [text.strip() for text in str(node).split('\n')]
    for i, line in enumerate(lines):
        if line:
            if line.startswith('#'):
                del lines[i]
            elif line[-1] != ':':
                lines[i] = line + ';'
    return ''.join(lines).strip()


class WarnRefactoringTool(refactor.RefactoringTool):

    def add_to_warnings(self, filename, fixer, node, new):
        fixer_name = fixer.__class__.__name__

        if not hasattr(self, 'warnings'):
            self.warnings = []
        warning = '%s -> %s' % (to_warn_str(node), to_warn_str(new))
        self.warnings.append((node.get_lineno(), '%s:%s:1: PY3K (%s) %s' % (
            filename, node.get_lineno(), fixer_name, warning)))

    def refactor_tree(self, tree, name):
        """Refactors a parse tree (modifying the tree in place).

        For compatible patterns the bottom matcher module is
        used. Otherwise the tree is traversed node-to-node for
        matches.

        Args:
            tree: a pytree.Node instance representing the root of the tree
                  to be refactored.
            name: a human-readable name for this tree.

        Returns:
            True if the tree was modified, False otherwise.
        """
        self.warnings = []

        for fixer in chain(self.pre_order, self.post_order):
            fixer.start_tree(tree, name)

        # use traditional matching for the incompatible fixers
        self.traverse_by(self.bmi_pre_order_heads, tree.pre_order())
        self.traverse_by(self.bmi_post_order_heads, tree.post_order())

        # obtain a set of candidate nodes
        match_set = self.BM.run(tree.leaves())

        while any(match_set.values()):
            for fixer in self.BM.fixers:
                if fixer in match_set and match_set[fixer]:
                    #sort by depth; apply fixers from bottom(of the AST) to top
                    match_set[fixer].sort(key=pytree.Base.depth, reverse=True)

                    if fixer.keep_line_order:
                        #some fixers(eg fix_imports) must be applied
                        #with the original file's line order
                        match_set[fixer].sort(key=pytree.Base.get_lineno)

                    for node in list(match_set[fixer]):
                        if node in match_set[fixer]:
                            match_set[fixer].remove(node)

                        try:
                            find_root(node)
                        except AssertionError:
                            # this node has been cut off from a
                            # previous transformation ; skip
                            continue

                        if node.fixers_applied and \
                           fixer in node.fixers_applied:
                            # do not apply the same fixer again
                            continue

                        results = fixer.match(node)

                        if results:
                            new = fixer.transform(node, results)
                            if new is not None:
                                node.replace(new)
                                self.add_to_warnings(name, fixer, node, new)
                                #new.fixers_applied.append(fixer)
                                for node in new.post_order():
                                    # do not apply the fixer again to
                                    # this or any subnode
                                    if not node.fixers_applied:
                                        node.fixers_applied = []
                                    node.fixers_applied.append(fixer)

                                # update the original match set for
                                # the added code
                                new_matches = self.BM.run(new.leaves())
                                for fxr in new_matches:
                                    if not fxr in match_set:
                                        match_set[fxr] = []

                                    match_set[fxr].extend(new_matches[fxr])

        for fixer in chain(self.pre_order, self.post_order):
            fixer.finish_tree(tree, name)
        return tree.was_changed


_rt = WarnRefactoringTool(refactor.get_fixers_from_package('py3kwarn2to3.fixes'))


def warnings_for_string(data, name):
    data += '\n'  # Silence certain parse errors
    tree = _rt.refactor_string(data, name)
    if tree and tree.was_changed:
        _rt.processed_file(str(tree), name, data)
        return sorted(_rt.warnings, key=lambda warning: warning[0])
    return []


def warnings_for_files(filenames):
    if not filenames:
        return []
    _rt.refactor(filenames)
    return sorted(_rt.warnings, key=lambda warning: warning[0])


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    import optparse
    parser = optparse.OptionParser(
        version='%prog {0}'.format(__version__),
        prog='py3kwarn')
    options, args = parser.parse_args(args)

    status = 0
    for warning in warnings_for_files(args):
        print(warning[1])
        status = 2

    return status
