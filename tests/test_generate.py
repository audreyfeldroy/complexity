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
        os.mkdir('tests/output/')

    def test_generate_html(self):
        generate.generate_html(input_dir='tests/input', output_dir='tests/output', context=None)
        self.assertTrue(os.path.isfile('tests/output/index.html'))
        self.assertTrue(os.path.isfile('tests/output/about/index.html'))

    def test_generate_context(self):
        context = generate.generate_context(input_dir='tests/input')
        self.assertEqual(context, {"test": {"1": 2}})

    def tearDown(self):
        shutil.rmtree('tests/output/')

if __name__ == '__main__':
    unittest.main()
