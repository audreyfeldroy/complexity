#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os

from complexity.generate import generate_context, generate_html
from complexity.serve import serve_static_site


def main():
    """ Entry point for the package, as defined in setup.py. """
    
    # Get command line input/output arguments
    parser = argparse.ArgumentParser(
        description='A refreshingly simple static site generator, for those who like to work in HTML.'
    )
    parser.add_argument(
        'input_dir',
        default='input/',
        help='Your project directory containing the files to be processed by Complexity.'
    )
    parser.add_argument(
        'output_dir',
        default='output/',
        help='Name of directory to output generated files to, e.g. www.'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=9090,
        help='Port number to serve files on.'
    )
    args = parser.parse_args()
    
    # List the stem of each input HTML file
    input_file_list = os.listdir(args.input_dir)
    pages = []
    for f in input_file_list:
        if f.endswith('html'):
            file_stem = f.split('.')[0]
            pages.append(file_stem)
    
    context = generate_context(args.input_dir)

    # Generate and serve the HTML site
    generate_html(args.input_dir, args.output_dir, pages, context)
    serve_static_site(args.output_dir, args.port)


if __name__ == '__main__':
    main()
