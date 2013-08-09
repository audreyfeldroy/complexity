#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.main
---------------

Main entry point for the `complexity` command.

The code in this module is also a good example of how to use Complexity as a
library rather than a script.
"""

import argparse
import os
import sys

from .conf import read_conf
from .generate import generate_context, copy_assets, generate_html
from .prep import prompt_and_delete_cruft
from .serve import serve_static_site


def complexity(project_dir):
    """
    API equivalent to using complexity at the command line.
    
    .. note:: You must delete `output_dir` before calling this. This also does
       not start the Complexity development server; you can do that from your
       code if desired.
    """

    # Get the configuration dictionary, if config exists
    defaults = {
        "templates_dir": "templates/",
        "assets_dir": "assets/",
        "context_dir": "context/",
        "output_dir": "../www/"
    }
    conf_dict = read_conf(project_dir) or defaults

    # Generate the context data
    context = None
    if 'context_dir' in conf_dict:
        context_dir = os.path.join(project_dir, conf_dict['context_dir'])
        if os.path.exists(context_dir):
            context = generate_context(context_dir)

    # Generate and serve the HTML site
    templates_dir = os.path.join(project_dir, conf_dict['templates_dir'])
    output_dir = os.path.join(project_dir, conf_dict['output_dir'])
    generate_html(templates_dir, output_dir, context)
    
    if 'assets_dir' in conf_dict:
        assets_dir = os.path.join(project_dir, conf_dict['assets_dir'])
        copy_assets(assets_dir, output_dir)


def get_complexity_args():
    """
    Get the command line input/output arguments passed in to Complexity.
    """
    
    parser = argparse.ArgumentParser(
        description='A refreshingly simple static site generator, for those'
        'who like to work in HTML.'
    )
    parser.add_argument(
        'project_dir',
        default='project/',
        help='Your project directory containing the files to be processed by'
        'Complexity.'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=9090,
        help='Port number to serve files on.'
    )
    args = parser.parse_args()
    return args


def main():
    """ Entry point for the package, as defined in `setup.py`. """

    args = get_complexity_args()

    # If output_dir exists, prompt before deleting.
    # Abort if it can't be deleted.
    if not prompt_and_delete_cruft(args.output_dir):
        sys.exit()

    output_dir = complexity(args.project_dir)
    serve_static_site(output_dir, args.port)
    

if __name__ == '__main__':
    main()
