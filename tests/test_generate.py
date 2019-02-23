#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_generate
--------------

Tests for `complexity.generate` module.
"""

import os
import shutil
import sys

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from complexity import generate

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class TestGetOutputFilename(unittest.TestCase):

    def test_get_output_filename(self):
        outfile = generate.get_output_filename(
            './index.html',
            'www',
            force_unexpanded=False
        )
        self.assertEqual(outfile, 'www/index.html')

    def test_get_output_filename_about(self):
        outfile = generate.get_output_filename(
            './about.html',
            'www',
            force_unexpanded=False
        )
        self.assertEqual(outfile, 'www/about/index.html')

    def test_get_output_filename_base(self):
        outfile = generate.get_output_filename(
            './base.html',
            'www',
            force_unexpanded=False
        )
        self.assertFalse(outfile)

    def test_get_output_filename_base_design(self):
        outfile = generate.get_output_filename(
            './base_design.html',
            'www',
            force_unexpanded=False
        )
        self.assertFalse(outfile)

    def test_get_output_filename_art(self):
        outfile = generate.get_output_filename(
            './art/index.html',
            'www',
            force_unexpanded=False
        )
        self.assertEqual(outfile, 'www/art/index.html')
        outfile = generate.get_output_filename(
            'art/index.html',
            'www',
            force_unexpanded=False
        )
        self.assertEqual(outfile, 'www/art/index.html')

    def test_get_output_filename_color(self):
        outfile = generate.get_output_filename(
            './art/color.html',
            'www',
            force_unexpanded=False
        )
        self.assertEqual(outfile, 'www/art/color/index.html')


class TestMinifyHTML(unittest.TestCase):
    def test_minify(self):
        raw_html = """<!DOCTYPE html>

        <html>
        <head>                   
        </head>
        <body>
            <p>Test!</p>
        </body>
        </html>"""
        expected = '<!DOCTYPE html><html><head></head><body>' \
                   '<p>Test!</p></body></html>'
        self.assertEqual(generate.minify_html(raw_html), expected)

    def test_minify_2(self):
        raw_html = """<!DOCTYPE html>

        <html>
        <head>
        </head>
        <body>
            <p>Test!</p>
            <p>Test2!</p>This should be left alone
            <p>Test3!</p>
                    As should this
        </body>
        </html>"""
        expected = """<!DOCTYPE html><html><head></head><body><p>Test!</p>""" \
            """<p>Test2!</p>This should be left alone
            <p>Test3!</p>

                    As should this

        </body></html>"""
        self.assertEqual(generate.minify_html(raw_html), expected)


class TestGenerateHTMLFile(unittest.TestCase):
    def setUp(self):
        os.mkdir('tests/www/')
        self.env = Environment()
        self.env.loader = FileSystemLoader('tests/project/templates/')

    def test_generate_html_file(self):
        generate.generate_html_file(
            template_filepath='index.html',
            output_dir='tests/www/',
            env=self.env,
            context={}
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertFalse(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))

    def test_generate_html_file_art(self):
        generate.generate_html_file(
            template_filepath='art/index.html',
            output_dir='tests/www/',
            env=self.env,
            context={}
        )
        self.assertTrue(os.path.isfile('tests/www/art/index.html'))
        self.assertFalse(os.path.isfile('tests/www/index.html'))
        self.assertFalse(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))

    def tearDown(self):
        shutil.rmtree('tests/www')


class TestGenerateHTMLFileUnicode(unittest.TestCase):
    def setUp(self):
        os.mkdir('tests/www/')
        self.env = Environment()
        self.env.loader = FileSystemLoader('tests/files/')

    def test_generate_html_file_unicode(self):
        generate.generate_html_file(
            template_filepath='unicode.html',
            output_dir='tests/www/',
            env=self.env,
            context={},
            minify=False
        )
        self.assertTrue(os.path.isfile('tests/www/unicode/index.html'))
        with open('tests/files/unicode.html') as infile:
            with open('tests/www/unicode/index.html') as outfile:
                self.assertEqual(infile.read(), outfile.read())

    def test_generate_html_file_unicode2(self):
        generate.generate_html_file(
            template_filepath='unicode2.html',
            output_dir='tests/www/',
            env=self.env,
            context={},
            minify=False
        )
        self.assertTrue(os.path.isfile('tests/www/unicode2/index.html'))
        expected = """<!DOCTYPE html>
<html>
<body>

<p>This is the unicode test page.</p>
<p>Polish: Ą Ł Ż</p>
<p>Chinese: 倀 倁 倂 倃 倄 倅 倆 倇 倈</p>
<p>Musical Notes: ♬ ♫ ♯</p>
<h3 class="panel-title">Paški sir</h3>
<p>Croatian: š š</p>

</body>
</html>"""
        with open('tests/www/unicode2/index.html') as outfile:
            self.assertEqual(expected, outfile.read())

    def test_generate_minified_html_file_unicode(self):
        generate.generate_html_file(
            template_filepath='unicode2.html',
            output_dir='tests/www/',
            env=self.env,
            context={},
            minify=True
        )
        self.assertTrue(os.path.isfile('tests/www/unicode2/index.html'))
        expected = '<!DOCTYPE html><html><body><p>This is the unicode test ' \
                   'page.</p><p>Polish: Ą Ł Ż</p><p>Chinese:' \
                   ' 倀 倁 倂 倃 倄 倅 倆 倇 倈</p><p>Musical Notes:' \
                   ' ♬ ♫ ♯</p><h3 class="panel-title">Paški sir</h3>' \
                   '<p>Croatian: š š</p></body></html>'
        with open('tests/www/unicode2/index.html') as outfile:
            self.assertEqual(expected, outfile.read())

    def tearDown(self):
        shutil.rmtree('tests/www')


class TestGenerateHTML(unittest.TestCase):
    def test_generate_html(self):
        generate.generate_html(
            templates_dir='tests/project/templates/',
            output_dir='tests/www/',
            context=None,
            unexpanded_templates=[]
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertTrue(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/color/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/cupcakes/index.html'))
        self.assertTrue(
            os.path.isfile('tests/www/art/cupcakes/chocolate/index.html')
        )
        self.assertFalse(os.path.isfile('tests/www/bad_templated_binary.png'))
        shutil.rmtree('tests/www')


class TestGenerateHTMLUnexpanded(unittest.TestCase):
    def test_generate_html_unexpanded(self):
        generate.generate_html(
            templates_dir='tests/project/templates/',
            output_dir='tests/www',
            context=None,
            unexpanded_templates=[
                '404.html',
                '500.html',
                "long/path/to/folder/dont-expand.html"
            ]
        )
        self.assertTrue(os.path.isfile('tests/www/index.html'))
        self.assertTrue(os.path.isfile('tests/www/about/index.html'))
        self.assertFalse(os.path.isfile('tests/www/base/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/color/index.html'))
        self.assertTrue(os.path.isfile('tests/www/art/cupcakes/index.html'))
        self.assertTrue(
            os.path.isfile('tests/www/art/cupcakes/chocolate/index.html')
        )
        self.assertTrue(os.path.isfile('tests/www/404.html'))
        self.assertTrue(os.path.isfile('tests/www/500.html'))
        self.assertTrue(
            os.path.isfile('tests/www/long/path/to/folder/dont-expand.html')
        )

    def tearDown(self):
        if os.path.isdir('tests/www'):
            shutil.rmtree('tests/www')


class TestGenerateContext(unittest.TestCase):
    def test_generate_context(self):
        context = generate.generate_context(
            context_dir='tests/project/context/'
        )
        self.assertEqual(context, {"test": {"1": 2}})


class TestCopyAssets(unittest.TestCase):
    def test_copy_assets(self):
        os.mkdir('tests/www/')
        generate.copy_assets(
            assets_dir='tests/project/assets/',
            output_dir='tests/www/'
        )
        self.assertTrue(
            os.path.isfile('tests/www/css/bootstrap-responsive.min.css')
        )
        self.assertTrue(os.path.isfile('tests/www/css/bootstrap.min.css'))
        self.assertTrue(
            os.path.isfile('tests/www/img/glyphicons-halflings.png')
        )
        self.assertTrue(os.path.isfile('tests/www/js/bootstrap.min.js'))
        self.assertTrue(os.path.isfile('tests/www/robots.txt'))
        shutil.rmtree('tests/www')


if __name__ == '__main__':
    unittest.main()
