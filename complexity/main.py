#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from complexity.generate import generate_context, generate_html
from complexity.serve import serve_static_site


def main():
    """ Entry point for the package, as defined in setup.py. """

    # List the stem of each HTML file in input/
    pages = [f.split('.')[0] for f in os.listdir('input/') if f.endswith('html')]

    context = generate_context()

    # Generate and serve the HTML site
    generate_html(pages, context)
    serve_static_site()


if __name__ == '__main__':
    main()
