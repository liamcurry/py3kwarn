# -*- coding: utf-8 -*-
import sys
import codecs
import logging
import os
import re
import shutil
import StringIO
import tempfile
import unittest

from py3kwarn2to3 import main


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
PY2_TEST_MODULE = os.path.join(TEST_DATA_DIR, "py2_test_grammar.py")


class TestMain(unittest.TestCase):

    if not hasattr(unittest.TestCase, 'assertNotRegex'):
        # This method was only introduced in 3.2.
        def assertNotRegex(self, text, regexp, msg=None):
            if not hasattr(regexp, 'search'):
                regexp = re.compile(regexp)
            if regexp.search(text):
                self.fail("regexp %s MATCHED text %r" % (regexp.pattern, text))

    def setUp(self):
        self.temp_dir = None  # tearDown() will rmtree this directory if set.

    def tearDown(self):
        # Clean up logging configuration down by main.
        del logging.root.handlers[:]
        if self.temp_dir:
            shutil.rmtree(self.temp_dir)

    def run_2to3_capture(self, args, in_capture, out_capture, err_capture):
        save_stdin = sys.stdin
        save_stdout = sys.stdout
        save_stderr = sys.stderr
        sys.stdin = in_capture
        sys.stdout = out_capture
        sys.stderr = err_capture
        try:
            return main.main("py3kwarn2to3.fixes", args)
        finally:
            sys.stdin = save_stdin
            sys.stdout = save_stdout
            sys.stderr = save_stderr

    def test_unencodable_diff(self):
        input_stream = StringIO.StringIO(u"print 'nothing'\nprint u'über'\n")
        out = StringIO.StringIO()
        out_enc = codecs.getwriter("ascii")(out)
        err = StringIO.StringIO()
        ret = self.run_2to3_capture(["-"], input_stream, out_enc, err)
        self.assertEqual(ret, 0)
        output = out.getvalue()
        self.assertTrue("-print 'nothing'" in output)
        self.assertTrue("WARNING: couldn't encode <stdin>'s diff for "
                        "your terminal" in err.getvalue())

    def setup_test_source_trees(self):
        """Setup a test source tree and output destination tree."""
        self.temp_dir = tempfile.mkdtemp()  # tearDown() cleans this up.
        self.py2_src_dir = os.path.join(self.temp_dir, "python2_project")
        self.py3_dest_dir = os.path.join(self.temp_dir, "python3_project")
        os.mkdir(self.py2_src_dir)
        os.mkdir(self.py3_dest_dir)
        # Turn it into a package with a few files.
        self.setup_files = []
        open(os.path.join(self.py2_src_dir, "__init__.py"), "w").close()
        self.setup_files.append("__init__.py")
        shutil.copy(PY2_TEST_MODULE, self.py2_src_dir)
        self.setup_files.append(os.path.basename(PY2_TEST_MODULE))
        self.trivial_py2_file = os.path.join(self.py2_src_dir, "trivial.py")
        self.init_py2_file = os.path.join(self.py2_src_dir, "__init__.py")
        with open(self.trivial_py2_file, "w") as trivial:
            trivial.write("print 'I need a simple conversion.'")
        self.setup_files.append("trivial.py")


if __name__ == '__main__':
    unittest.main()
