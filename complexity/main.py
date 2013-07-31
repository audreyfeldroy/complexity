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

from .generate import generate_context, copy_assets, generate_html
from .prep import prompt_and_delete_cruft
from .serve import serve_static_site


class ComplexitySite(object):
    """
    The central object holding all essential state for a Complexity site.
    """
    
    def __init__(self, templates_dir="templates", assets_dir="assets",
                 output_dir="../www"):
        """
        Initialize all variables holding Complexity state.
        """
        
        self.templates_dir = templates_dir
        self.assets_dir = assets_dir
        self.output_dir = output_dir


def complexity(project_dir, output_dir):
    """
    API equivalent to using complexity at the command line.
    
    .. note:: You must delete `output_dir` before calling this. This also does
       not start the Complexity development server; you can do that from your
       code if desired.
    """

    # Generate the context data
    json_dir = os.path.join(project_dir, 'json/')

    context = None
    if os.path.exists(json_dir):
        context = generate_context(json_dir)

    # Generate and serve the HTML site
    templates_dir = os.path.join(project_dir, 'templates/')
    generate_html(templates_dir, output_dir, context)
    
    assets_dir = os.path.join(project_dir, 'assets/')
    copy_assets(assets_dir, output_dir)


def main():
    """ Entry point for the package, as defined in `setup.py`. """

    # Get command line input/output arguments
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
        'output_dir',
        default='www/',
        help='Name of directory to output generated files to, e.g. www.'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=9090,
        help='Port number to serve files on.'
    )
    args = parser.parse_args()

    # If output_dir exists, prompt before deleting.
    # Abort if it can't be deleted.
    if not prompt_and_delete_cruft(args.output_dir):
        sys.exit()

    complexity(args.project_dir, args.output_dir)
    serve_static_site(args.output_dir, args.port)
    

if __name__ == '__main__':
    main()
