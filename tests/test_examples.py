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

from complexity.main import complexity


class TestExamples(unittest.TestCase):

    def test_complexity_example(self):
        """
        Tests that https://github.com/audreyr/complexity-example.git works.
        """
        os.system('git clone https://github.com/audreyr/complexity-example.git')
        complexity('complexity-example/project/', 'complexity-example/www/')
        self.assertTrue(os.path.isfile('complexity-example/www/index.html'))
        self.assertTrue(os.path.isfile('complexity-example/www/about/index.html'))
        self.assertTrue(os.path.isfile('complexity-example/www/img/glyphicons-halflings.png'))
        shutil.rmtree('complexity-example')

if __name__ == '__main__':
    unittest.main()
