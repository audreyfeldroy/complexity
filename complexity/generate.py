#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import string

from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from complexity.utils import make_sure_path_exists, unicode_open


def render_and_write_html_file(f, output_dir, env, context):
    """
        Renders and writes a single HTML file to its corresponding output location.
    """

    if not f.endswith('html'):
        raise TypeError(
            'Non-HTML template found. Make sure all files in templates/ are .html files.'
        )

    # Ignore any template starting with "base". 
    # Complexity treats them as special cases.
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
        output_filename = os.path.join(output_dir, '{0}/index.html'.format(stem))
        make_sure_path_exists(os.path.dirname(output_filename))

    # Write the generated file
    with unicode_open(output_filename, 'w') as fh:
        fh.write(rendered_html)
        return True


def generate_html(input_dir, output_dir, context=None):
    """
    Renders the HTML templates from input_dir, and writes them to output_dir.
    """
            
    context = context or {}
    env = Environment()
    env.loader = FileSystemLoader(input_dir)

    # Create the output dir if it doesn't already exist
    make_sure_path_exists(output_dir)

    # input_file_list = os.listdir(input_dir)
            
    # for f in input_file_list:
    
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            render_and_write_html_file(f, output_dir, env, context)


def generate_context(input_dir):
    """
    Generates the context for all complexity pages.

    Description:

        Iterates through the contents of the input_dir and finds all JSON files.
        Loads the JSON file as a Python object with the key being the JSON file name.

    Example:

        Assume the following files exist:

            input/names.json
            input/numbers.json

        Depending on their content, might generate a context as follows:

        contexts = {"names":
                        ['Audrey', 'Danny']
                    "numbers":
                        [1, 2, 3, 4]
                    }
    """
    context = {}
    
    all_input_files = os.listdir(input_dir)

    for file_name in all_input_files:
        
        if file_name.endswith('json'):

            # Open the JSON file and convert to Python object
            json_file = "{0}/{1}".format(input_dir, file_name)
            with unicode_open(json_file) as f:
                obj = json.load(f)

            # Add the Python object to the context dictionary
            context[file_name[:-5]] = obj

    return context
