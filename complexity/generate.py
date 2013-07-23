#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import shutil

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from .exceptions import NonHTMLFileException, MissingTemplateDirException
from .utils import make_sure_path_exists, unicode_open


def generate_html_file(f, output_dir, env, context):
    """
    Renders and writes a single HTML file to its corresponding output location.
    
    :param f: Name of input file to be rendered.
    :param output_dir: The Complexity www (output) directory.
    :paramtype output_dir: directory
    :param env: Jinja2 environment with a loader already set up.
    :param context: Jinja2 context that holds template variables. See
        http://jinja.pocoo.org/docs/api/#the-context
    """

    if not f.endswith('html'):
        raise NonHTMLFileException(
            'Non-HTML file found. Make sure all files in templates/ are \
            .html files.'
        )

    # Ignore templates starting with "base". They're treated as special cases.
    if f.startswith('base'):
        return False

    tmpl = env.get_template(f)
    rendered_html = tmpl.render(**context)

    # Put index in the root. It's a special case.
    if f == 'index.html':
        output_filename = os.path.join(output_dir, 'index.html')
    # Put other pages in page/index.html, for better URL formatting.
    else:
        stem = f.split('.')[0]
        output_filename = os.path.join(
            output_dir,
            '{0}/index.html'.format(stem)
        )
        make_sure_path_exists(os.path.dirname(output_filename))

    # Write the generated file
    with unicode_open(output_filename, 'w') as fh:
        fh.write(rendered_html)
        return True


def generate_html(input_dir, output_dir, context=None):
    """
    Renders the HTML templates from input_dir, and writes them to output_dir.
    
    :param input_dir: The Complexity project (input) directory.
    :paramtype input_dir: directory
    :param output_dir: The Complexity www (output) directory.
    :paramtype output_dir: directory
    :param context: Jinja2 context that holds template variables. See
        http://jinja.pocoo.org/docs/api/#the-context
    """

    templates_dir = os.path.join(input_dir, 'templates/')
    if not os.path.exists(templates_dir):
        raise MissingTemplateDirException(
            'Your project is missing a templates/ directory containing your \
            HTML templates.'
        )

    context = context or {}
    env = Environment()
    env.loader = FileSystemLoader(templates_dir)

    # Create the output dir if it doesn't already exist
    make_sure_path_exists(output_dir)

    for root, dirs, files in os.walk(templates_dir):
        for f in files:
            print(f)
            generate_html_file(f, output_dir, env, context)


def generate_context(json_dir):
    """
    Generates the context for all complexity pages.
    
    :param json_dir: Directory containing .json file(s).
    :paramtype json_dir: directory

    Description:

        Iterates through the contents of json_dir and finds all JSON
        files. Loads the JSON file as a Python object with the key being the
        JSON file name.

    Example:

        Assume the following files exist:

            json/names.json
            json/numbers.json

        Depending on their content, might generate a context as follows:

        contexts = {"names":
                        ['Audrey', 'Danny']
                    "numbers":
                        [1, 2, 3, 4]
                    }
    """
    context = {}

    json_files = os.listdir(json_dir)

    for file_name in json_files:

        if file_name.endswith('json'):

            # Open the JSON file and convert to Python object
            json_file = os.path.join(json_dir, file_name)
            with unicode_open(json_file) as f:
                obj = json.load(f)

            # Add the Python object to the context dictionary
            context[file_name[:-5]] = obj

    return context


def copy_assets(input_dir, output_dir):
    """
    Copies static assets over from input_dir/assets/ to output_dir/.
    
    :param input_dir: The Complexity project (input) directory.
    :paramtype input_dir: directory
    :param output_dir: The Complexity www (output) directory.
    :paramtype output_dir: directory
    """
    assets = os.path.join(input_dir, 'assets')
    all_asset_dirs = os.listdir(assets)
    for d in all_asset_dirs:
        old_dir = os.path.join(assets, d)

        # Only copy allowed dirs
        if os.path.isdir(old_dir) and d != 'scss' and d != 'less':
            new_dir = os.path.join(output_dir, d)
            print('Copying {0} to {1}'.format(d, new_dir))
            shutil.copytree(old_dir, new_dir)
