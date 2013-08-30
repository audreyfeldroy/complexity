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
import logging
import os
import sys

from .conf import read_conf, get_unexpanded_list
from .exceptions import OutputDirExistsException
from .generate import generate_context, copy_assets, generate_html
from .prep import prompt_and_delete_cruft
from .serve import serve_static_site


logger = logging.getLogger(__name__)

def complexity(project_dir, no_input=True):
    """
    API equivalent to using complexity at the command line.

    :param project_dir: The Complexity project directory, e.g. `project/`.
    :paramtype project_dir: directory

    :param no_input: If true, don't prompt about whether to delete
        pre-existing `www/` directory. Instead, throw exception if one is
        found.

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

    output_dir = os.path.normpath(
        os.path.join(project_dir, conf_dict['output_dir'])
    )

    # If output_dir exists, prompt before deleting.
    # Abort if it can't be deleted.
    if no_input:
        if os.path.exists(output_dir):
            raise OutputDirExistsException(
                'Please delete {0} manually and try again.'
            )
    else:
        if not prompt_and_delete_cruft(output_dir):
            sys.exit()

    # Generate the context data
    context = None
    if 'context_dir' in conf_dict:
        context_dir = os.path.join(project_dir, conf_dict['context_dir'])
        if os.path.exists(context_dir):
            context = generate_context(context_dir)

    # Generate and serve the HTML site
    unexpanded_templates = get_unexpanded_list(conf_dict)
    templates_dir = os.path.join(project_dir, conf_dict['templates_dir'])
    generate_html(templates_dir, output_dir, context, unexpanded_templates)

    if 'assets_dir' in conf_dict:
        assets_dir = os.path.join(project_dir, conf_dict['assets_dir'])
        copy_assets(assets_dir, output_dir)

    return output_dir


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
    parser.add_argument(
        '--noserver',
        action='store_true',
        help='Don\'t run the server.'
    )
    args = parser.parse_args()
    return args


def main():
    """ Entry point for the package, as defined in `setup.py`. """

    args = get_complexity_args()

    output_dir = complexity(project_dir=args.project_dir, no_input=False)
    if not args.noserver:
        serve_static_site(output_dir=output_dir, port=args.port)


if __name__ == '__main__':
    main()
