from itertools import chain
from lib2to3 import refactor, pytree
from lib2to3.fixer_util import find_root
from lib2to3.fixes import fix_imports, fix_imports2, fix_methodattrs


FIXER_WARNINGS = {
    'apply': ('apply(func, args, kwargs)', 'func(*args, **kwargs)'),
    'basestring': ('basestring', 'str'),
    'buffer': ('buffer(...)', 'memoryview(...)'),
    'callable': ('callable(obj)', 'isinstance(obj, collections.Callable)'),
    'dict': {
        'iterkeys': ('d.iterkeys()', 'iter(d.keys())'),
        'iteritems': ('d.iteritems()', 'iter(d.items())'),
        'itervalues': ('d.itervalues()', 'iter(d.values())'),
        'viewkeys': ('d.viewkeys()', 'd.keys()'),
        'viewitems': ('d.viewitems()', 'd.items()'),
        'viewvalues': ('d.viewvalues()', 'd.values()'),
        'keys': ('d.keys()', 'list(d.keys())'),
        'items': ('d.items()', 'list(d.items())'),
        'values': ('d.values()', 'list(d.values())'),
    },
    'except': '',
    'exec': ('exec code in ns1, ns2', 'exec(code, ns1, ns2)'),
    'execfile': ('execfile("foobar.py")', 'exec(compile(open("foobar.py").read(), "foobar.py", "exec")'),
    'exitfunc': ('sys.exitfunc', 'sys.atexit'),
    'filter': ('filter(F, X)', 'list(filter(F, X))'),
    'funcattrs': {
        'closure': ('f.func_closure', 'f.__closure__'),
        'doc': ('f.func_doc', 'f.__doc__'),
        'globals': ('f.func_globals', 'f.__globals__'),
        'name': ('f.func_name', 'f.__name__'),
        'defaults': ('f.func_name', 'f.__name__'),
        'code': ('f.func_code', 'f.__code__'),
        'dict': ('f.func_dict', 'f.__dict__'),
    },
    'future': "'__future__' imports are removed in Python 3",
    'getcwdu': ('getcwdu', 'getcwd'),
    'haskey': ('d.has_key("foobar")', '"foobar" in d'),
    'idioms': {
        '==': ('type(x) == T', 'isinstance(x, T)'),
        '!=': ('type(x) != T', 'not isinstance(x, T)'),
        'is not': ('type(x) is not T', 'not isinstance(x, T)'),
        'is': ('type(x) is T', 'isinstance(x, T)'),
        'while': ('while 1:', 'while True:'),
        'sort': 'Use the "sorted" method'
    },
    'import': 'Absolute imports should not be used for sibling modules; use relative imports instead.',
    'imports': fix_imports.MAPPING,
    'imports2': fix_imports2.MAPPING,
    'input': ('input(...)', 'eval(input(...))'),
    'intern': ('intern(x)', 'sys.itern(x)'),
    'isinstance': {
        'long': ('instance(x, (int, long))', 'instance(x, int)'),
        'int': ('instance(x, (int, int))', 'instance(x, int)'),
    },
    'itertoolsimports': '',
    'itertools': {
        'imap': ('itertools.imap', 'itertools.map'),
        'ifilter': ('itertools.ifilter', 'itertools.filter'),
        'izip': ('itertools.izip', 'itertools.map'),
        'ifilterfalse': ('itertools.ifilterfalse', 'itertools.filterfalse'),
    },
    'long': ('long', 'int'),
    'map': {
        'None': ('map(None, x)', 'list(x)'),
        'map': ('map(x, ...)', 'list(map(x, ...))'),
    },
    'metaclass': ('__metaclass__ = x', '(metaclass=x)'),
    'methodattrs': fix_methodattrs.MAP,
    'ne': ('<>', '!='),
    'next': ('x.next()', 'next(x)'),
    'nonzero': ('__nonzero', '__bool__'),
    'numliterals': {
        'l': ('1L', '1'),
        '0': ('0755', '0o755')
    },
    'operator': {
        'isCallable': ('operator.isCallable(obj)', 'hasattr(obj, "__call__")'),
        'sequenceIncludes': ('operator.sequenceIncludes(obj)', 'operator.contains(obj)'),
        'isSequenceType': ('operator.isSequenceType(obj)', 'isinstance(obj, collections.Sequence)'),
        'isMappingType': ('operator.isMappingType(obj)', 'isinstance(obj, collections.Mapping)'),
        'isNumberType': ('operator.isNumberType(obj)', 'isinstance(obj, numbers.Number)'),
        'irepeat': ('operator.repeat(obj, n)', 'operator.imul(obj, n)'),
        'repeat': ('operator.repeat(obj, n)', 'operator.mul(obj, n)'),
    },
    'paren': ('[x for x in 1, 2]', '[x for x in (1, 2)]'),
    'print': ('print ...', 'print(...)'),
    'raise': '',
    'raw_input': '',
    'reduce': '',
    'renames': '',
    'repr': '',
    'set_literal': '',
    'standarderror': '',
    'sys_exc': '',
    'throw': '',
    'tuple_params': '',
    'types': '',
    'unicode': {
        'unicode': ('unicode', 'str'),
        'unichr': ('unichar', 'chr'),
        'u\'': ('u"..."', '"..."'),
        'u"': ('u"..."', '"..."'),
    },
    'urllib': '',
    'wscomma': '',
    'xrange': '',
    'xreadlines': '',
    'zip': ''
}


def to_warn_str(node):
    lines = str(node).split('\n')
    for i, l in enumerate(lines):
        if l.startswith('#'):
            del lines[i]
    return to_one_line(lines)


def to_one_line(lines):
    string = ''
    for line in lines:
        line = line.strip()
        if line:
            if line[-1] == ':':
                string += line + ' '
            else:
                string += line + '; '
    return string


class WarnRefactoringTool(refactor.RefactoringTool):

    def add_to_warnings(self, filename, fixer, node, new):
        if not hasattr(self, 'warnings'):
            self.warnings = []
        fixer_name = fixer.__class__.__name__.lower()[3:]
        warning = '%s -> %s' % (to_warn_str(node), to_warn_str(new))
        #warning = FIXER_WARNINGS.get(fixer_name, fixer_name)
        #if isinstance(warning, dict):
        #    for key, val in warning.items():
        #        if key in str(node):
        #            warning = val
        #            break
        #if isinstance(warning, tuple):
        #    warning = '%s -> %s' % warning
        #if not warning or not isinstance(warning, str):
        #    warning = fixer_name
        self.warnings.append((node.get_lineno(), '%s:%s: PY3K (%s) %s' % (filename, node.get_lineno(), fixer_name, warning)))

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

        #use traditional matching for the incompatible fixers
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

                        if node.fixers_applied and fixer in node.fixers_applied:
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


if __name__ == '__main__':
    import sys
    rt = WarnRefactoringTool(refactor.get_fixers_from_package('lib2to3.fixes'))
    #rt.refactor(['/Users/cygni/Dropbox/Workspace/WP/projects/wp-ad-flightmanager/apps/flights/models.py', ])
    rt.refactor([sys.argv[1], ])
    warnings = sorted(rt.warnings, key=lambda warning: warning[0])
    for warning in warnings:
        print warning[1]
