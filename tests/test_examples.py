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


class TestExample(unittest.TestCase):

    def setUp(self):
        os.system(
            'git clone https://github.com/audreyr/complexity-example.git'
        )

    def test_complexity_example(self):
        """
        Tests that https://github.com/audreyr/complexity-example.git works.
        """

        complexity('complexity-example/project/')
        self.assertTrue(os.path.isfile('complexity-example/www/index.html'))
        self.assertTrue(
            os.path.isfile('complexity-example/www/about/index.html')
        )
        self.assertTrue(
            os.path.isfile(
                'complexity-example/www/img/glyphicons-halflings.png'
            )
        )

    def tearDown(self):
        shutil.rmtree('complexity-example')


class TestExample2(unittest.TestCase):

    def setUp(self):
        os.system(
            'git clone https://github.com/audreyr/complexity-example2.git'
        )

    def test_complexity_example(self):
        """
        Tests that https://github.com/audreyr/complexity-example2.git works.
        """

        complexity('complexity-example2/project/')
        self.assertTrue(
            os.path.isfile('complexity-example2/www/index.html')
        )
        self.assertTrue(os.path.isfile(
            'complexity-example2/www/about/index.html')
        )
        self.assertTrue(
            os.path.isfile('complexity-example2/www/repos/index.html')
        )
        self.assertTrue(
            os.path.isfile(
                'complexity-example2/www/img/glyphicons-halflings.png'
            )
        )
        self.assertTrue(
            os.path.isfile('complexity-example2/www/charts/index.html')
        )
        self.assertTrue(
            os.path.isfile('complexity-example2/www/charts/bar/index.html')
        )
        self.assertTrue(
            os.path.isfile('complexity-example2/www/charts/pie/index.html')
        )
        self.assertTrue(
            os.path.isfile(
                'complexity-example2/www/charts/pie/basic/index.html'
            )
        )
        self.assertTrue(
            os.path.isfile(
                'complexity-example2/www/charts/pie/donut/index.html'
            )
        )

    def tearDown(self):
        shutil.rmtree('complexity-example2')

if __name__ == '__main__':
    unittest.main()
