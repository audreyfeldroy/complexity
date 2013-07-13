#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_complexity
------------

Tests for `complexity` module.
"""

from complexity import complexity
import unittest


class TestComplexity(unittest.TestCase):

    def test_make_sure_path_exists(self):
        self.assertTrue(complexity.make_sure_path_exists('/usr/'))
        self.assertFalse(
            complexity.make_sure_path_exists(
                '/this-dir-does-not-exist-and-cant-be-created/'
            )
        )

if __name__ == '__main__':
    unittest.main()
