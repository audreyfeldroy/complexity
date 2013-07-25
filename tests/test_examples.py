#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_examples
--------------

Tests for the Complexity example repos.
"""

import os
import shutil
import unittest

from complexity import complexity


class TestExamples(unittest.TestCase):

    def test_complexity_example(self):
        """
        Tests that https://github.com/audreyr/complexity-example.git works.
        """
        os.system('git clone https://github.com/audreyr/complexity-example.git')
        os.chdir('complexity-example')
        complexity('project/', 'www/')
        self.assertTrue(os.path.isfile('www/index.html'))
        self.assertTrue(os.path.isfile('www/about/index.html'))
        self.assertTrue(os.path.isfile('www/css/bootstrap.min.css'))
        self.assertTrue(os.path.isfile('www/js/bootstrap.min.js'))
        self.assertTrue(os.path.isfile('www/img/glyphicons-halflings.png'))
        os.chdir(os.pardir)
        shutil.rmtree('complexity-example')

if __name__ == '__main__':
    unittest.main()
