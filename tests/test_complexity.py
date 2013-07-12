#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_complexity
------------

Tests for `complexity` module.
"""

import complexity
import unittest

class TestComplexity(unittest.TestCase):

    def test_make_sure_path_exists(self):
        self.assertTrue(complexity.make_sure_path_exists('/usr/'))
        self.assertFalse(
            complexity.make_sure_path_exists(
                '/it-would-be-really-weird-if-this-directory-existed/'
            )
        )

if __name__ == '__main__':
    unittest.main()
