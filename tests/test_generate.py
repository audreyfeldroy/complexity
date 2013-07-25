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

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from complexity import generate


class TestGenerate(unittest.TestCase):

    def test_get_output_filename(self):
        outfile = generate.get_output_filename('./index.html', 'www')
        self.assertEqual(outfile, 'www/index.html')

    def test_get_output_filename_about(self):
        outfile = generate.get_output_filename('./about.html', 'www')
        self.assertEqual(outfile, 'www/about/index.html')

    def test_get_output_filename_base(self):
        outfile = generate.get_output_filename('./base.html', 'www')
        self.assertFalse(outfile)

    def test_get_output_filename_base_design(self):
        outfile = generate.get_output_filename('./base_design.html', 'www')
        self.assertFalse(outfile)

    def test_get_output_filename_art(self):
        outfile = generate.get_output_filename('./art/index.html', 'www')
        self.assertEqual(outfile, 'www/art/index.html')
        outfile = generate.get_output_filename('art/index.html', 'www')
        self.assertEqual(outfile, 'www/art/index.html')

    def test_get_output_filename_color(self):
        outfile = generate.get_output_filename('./art/color.html', 'www')
        self.assertEqual(outfile, 'www/art/color/index.html')

    def test_generate_html_file(self):
        os.mkdir('tests/www/')
        env = Environment()
        env.loader = FileSystemLoader('tests/project/templates/')
        generate.generate_html_file(
            template_filepath='index.html', 
            output_dir='tests/www/',
            env=env,
            context={}
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertFalse(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        shutil.rmtree('tests/www')

    def test_generate_html_file_art(self):
        os.mkdir('tests/www/')
        env = Environment()
        env.loader = FileSystemLoader('tests/project/templates/')
        generate.generate_html_file(
            template_filepath='art/index.html', 
            output_dir='tests/www/',
            env=env,
            context={}
        )
        self.assertTrue(os.path.isfile('tests/www/art/index.html'))
        self.assertFalse(os.path.isfile('tests/www/index.html'))
        self.assertFalse(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        shutil.rmtree('tests/www')

    def test_generate_html(self):
        generate.generate_html(
            templates_dir='tests/project/templates/',
            output_dir='tests/www/',
            context=None
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertTrue(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/color/index.html'))
        shutil.rmtree('tests/www')

    def test_generate_context(self):
        context = generate.generate_context(json_dir='tests/project/json/')
        self.assertEqual(context, {"test": {"1": 2}})

    def test_copy_assets(self):
        generate.copy_assets(
            assets_dir='tests/project/assets/',
            output_dir='tests/www/'
        )
        self.assertTrue(os.path.isfile('tests/www/css/bootstrap-responsive.min.css'))
        self.assertTrue(os.path.isfile('tests/www/css/bootstrap.min.css'))
        self.assertTrue(os.path.isfile('tests/www/img/glyphicons-halflings.png'))
        self.assertTrue(os.path.isfile('tests/www/js/bootstrap.min.js'))
        self.assertTrue(os.path.isfile('tests/www/robots.txt'))
        shutil.rmtree('tests/www')


if __name__ == '__main__':
    unittest.main()
