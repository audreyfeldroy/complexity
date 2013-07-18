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

    def test_generate_html(self):
        generate.generate_html(
            input_dir='tests/project/',
            output_dir='tests/www/',
            context=None
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertTrue(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        shutil.rmtree('tests/www')

    def test_generate_context(self):
        context = generate.generate_context(input_dir='tests/project/json/')
        self.assertEqual(context, {"test": {"1": 2}})

if __name__ == '__main__':
    unittest.main()
