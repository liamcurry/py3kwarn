# coding=utf-8

from __future__ import print_function
from __future__ import unicode_literals

from itertools import chain
import sys

from . import __version__

from py3kwarn2to3 import refactor, pytree
from py3kwarn2to3.fixer_util import find_root


try:
    unicode
except NameError:
    unicode = str


def to_warn_str(node):
    lines = [text.strip() for text in unicode(node).split('\n')]
    for i, line in enumerate(lines):
        if line:
            if line.startswith('#'):
                del lines[i]
            elif line[-1] != ':':
                lines[i] = line + ';'
    return ''.join(lines).strip()


class WarnRefactoringTool(refactor.MultiprocessRefactoringTool):

    def __init__(self, fixer_names, options=None, explicit=None):
        super(WarnRefactoringTool, self).__init__(
            fixer_names, options, explicit)

        self.warnings = []

    def _append_warning(self, warning):
        self.warnings.append(warning)

    def add_to_warnings(self, filename, fixer, node, new):
        fixer_name = fixer.__class__.__name__

        from_string = to_warn_str(node)
        to_string = to_warn_str(new)

        warning = '{0} -> {1}'.format(from_string, to_string)
        self._append_warning((
            node.get_lineno(),
            '{filename}:{line}:1: PY3K ({fixer}) {warning}'.format(
                filename=filename,
                line=node.get_lineno(),
                fixer=fixer_name,
                warning=warning)))

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
                    # sort by depth; apply fixers from bottom(of the AST) to
                    # top
                    match_set[fixer].sort(key=pytree.Base.depth, reverse=True)

                    if fixer.keep_line_order:
                        # some fixers(eg fix_imports) must be applied
                        # with the original file's line order
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
                            original_node = node.clone()
                            new = fixer.transform(node, results)
                            if new is not None:
                                node.replace(new)
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

                            new = new or node
                            if new != original_node:
                                self.add_to_warnings(name,
                                                     fixer,
                                                     original_node,
                                                     new)

        for fixer in chain(self.pre_order, self.post_order):
            fixer.finish_tree(tree, name)
        return tree.was_changed


def warnings_for_string(data, name=''):
    tool = WarnRefactoringTool(
        refactor.get_fixers_from_package(
            'py3kwarn2to3.fixes'))
    data += '\n'  # Silence certain parse errors
    tree = tool.refactor_string(data, name)
    if tree and tree.was_changed:
        tool.processed_file(unicode(tree), name, data)
        return sorted(tool.warnings, key=lambda warning: warning[0])
    return []


class PrintWarnRefactoringTool(WarnRefactoringTool):

    """WarnRefactoringTool that prints to standard out."""

    def _append_warning(self, warning):
        super(PrintWarnRefactoringTool, self)._append_warning(warning)

        print(warning[1])

    def refactor_tree(self, tree, name):
        super(PrintWarnRefactoringTool, self).refactor_tree(tree, name)

        sys.stdout.flush()


def print_warnings_for_files(filenames, num_processes=1):
    """Print warnings to standard out.

    Return number of warnings.

    """
    if not filenames:
        return 0

    tool = PrintWarnRefactoringTool(refactor.get_fixers_from_package(
        'py3kwarn2to3.fixes'))

    if filenames == ['-']:
        tool.refactor_stdin()
    else:
        tool.refactor(filenames,
                      num_processes=num_processes)

    return len(tool.warnings)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    import optparse
    parser = optparse.OptionParser(version='%prog {0}'.format(__version__),
                                   prog='py3kwarn')
    parser.add_option('-j', '--jobs', action='store', default=1,
                      type='int', help='Run in parallel')
    options, args = parser.parse_args(args)

    if options.jobs < 1:
        try:
            import multiprocessing
        except ImportError:
            parser.error('"--jobs" is not supported on this platform')
        options.jobs = multiprocessing.cpu_count()

    return 2 if print_warnings_for_files(args,
                                         num_processes=options.jobs) else 0
