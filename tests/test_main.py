#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_main
----------------

Tests for `complexity.main` module.
"""

import os
import shutil
import unittest

from complexity import main


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


if __name__ == '__main__':
    unittest.main()
