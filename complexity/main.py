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

from . import complexity
from .prep import prompt_and_delete_cruft
from .serve import serve_static_site


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
