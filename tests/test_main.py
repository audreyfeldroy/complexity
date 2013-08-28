#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
----------------

Tests for `complexity.main` module.
"""

import logging
import os
import shutil
import sys

from complexity import main

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


# Log debug and above to console
# logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class TestMain(unittest.TestCase):

    def test_get_complexity_args(self):
        """ TODO: figure out how to test argparse here. """
        pass


class TestConfProj(unittest.TestCase):

    def test_conf_proj_with_complexity(self):
        main.complexity('tests/conf_proj')
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertTrue(os.path.isfile('tests/www/about/index.html'))

    def tearDown(self):
        if os.path.isdir('tests/www'):
            shutil.rmtree('tests/www')


class TestConfProj2(unittest.TestCase):

    def test_conf_proj2_with_complexity(self):
        main.complexity('tests/conf_proj2')
        self.assertTrue(os.path.isfile('tests/conf_proj2/wwwz/index.html'))
        self.assertTrue(
            os.path.isfile('tests/conf_proj2/wwwz/about/index.html')
        )

    def tearDown(self):
        if os.path.isdir('tests/conf_proj2/wwwz'):
            shutil.rmtree('tests/conf_proj2/wwwz')


if __name__ == '__main__':
    unittest.main()
