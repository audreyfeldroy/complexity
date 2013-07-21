#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import sys

from .generate import generate_context, copy_assets, generate_html
from .prep import prompt_and_delete_cruft
from .serve import serve_static_site


def main():
    """ Entry point for the package, as defined in setup.py. """

    # Get command line input/output arguments
    parser = argparse.ArgumentParser(
        description='A refreshingly simple static site generator, for those'
        'who like to work in HTML.'
    )
    parser.add_argument(
        'input_dir',
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

    # Generate the context data
    json_dir = os.path.join(args.input_dir, 'json/')

    context = None
    if os.path.exists(json_dir):
        context = generate_context(json_dir)

    # Generate and serve the HTML site
    generate_html(args.input_dir, args.output_dir, context)
    copy_assets(args.input_dir, args.output_dir)
    serve_static_site(args.output_dir, args.port)


if __name__ == '__main__':
    main()
