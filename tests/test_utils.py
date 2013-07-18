#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_utils
------------

Tests for `complexity.utils` module.
"""

import os
import shutil
import unittest

from complexity import generate, utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        os.mkdir('output/')

    def test_make_sure_path_exists(self):
        self.assertTrue(utils.make_sure_path_exists('/usr/'))
        self.assertFalse(
            utils.make_sure_path_exists(
                '/this-dir-does-not-exist-and-cant-be-created/'
            )
        )

    def test_unicode_open(self):
        """ Test unicode_open(filename, *args, **kwargs). """

        unicode_text = """Polish: Ą Ł Ż
Chinese: 倀 倁 倂 倃 倄 倅 倆 倇 倈
Musical Notes: ♬ ♫ ♯"""

        with utils.unicode_open('tests/files/unicode.txt') as f:
            opened_text = f.read()
            self.assertEqual(unicode_text, opened_text)

    def tearDown(self):
        shutil.rmtree('output/')

if __name__ == '__main__':
    unittest.main()
