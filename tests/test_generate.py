#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_generate
--------------

Tests for `complexity.generate` module.
"""

import os
import shutil
import unittest

from complexity import generate


class TestGenerate(unittest.TestCase):

    def setUp(self):
        # os.chdir('tests/')
        os.mkdir('output/')

    def test_generate_html(self):
        generate.generate_html(['index', 'about'], context=None, input_dir='tests/input')
        self.assertTrue(os.path.isfile('output/index.html'))
        self.assertTrue(os.path.isfile('output/about/index.html'))

    def test_generate_context(self):
        context = generate.generate_context(input_dir='tests/input')
        self.assertEqual(context, {"test": {"1": 2}})

    def tearDown(self):
        shutil.rmtree('output/')

if __name__ == '__main__':
    unittest.main()
