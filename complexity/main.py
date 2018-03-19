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
import time

from .conf import read_conf, get_unexpanded_list, DEFAULTS
from .exceptions import OutputDirExistsException
from .generate import generate_context, copy_assets, generate_html
from .prep import prompt_and_delete_cruft, delete_cruft
from .serve import serve_static_site

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import gmtime, strftime

logger = logging.getLogger(__name__)


def _get_dir(project_dir, conf_dir_name):
    conf_dict = read_conf(project_dir) or DEFAULTS
    output_dir = os.path.normpath(
        os.path.join(project_dir, conf_dict[conf_dir_name])
    )
    return output_dir


def _get_output_dir(project_dir):
    return _get_dir(project_dir, 'output_dir')


def complexity(project_dir, overwrite=False, no_input=True, quiet=False, _leave_output=False):
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

    :para quiet: if True, we won't alert the end user to anything, and we'll
    `just run` until we are finished
    """

    # Get the configuration dictionary, if config exists
    conf_dict = read_conf(project_dir) or DEFAULTS

    output_dir = _get_output_dir(project_dir)

    if overwrite:
        delete_cruft(output_dir, only_contents=_leave_output)
    elif no_input:
        # If output_dir exists, prompt before deleting.
        # Abort if it can't be deleted.
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
    macros_dir = os.path.join(project_dir, conf_dict['macros_dir'])

    generate_html(templates_dir, macros_dir, output_dir,
                  context, unexpanded_templates, conf_dict['expand'], quiet)

    if 'assets_dir' in conf_dict:
        assets_dir = os.path.join(project_dir, conf_dict['assets_dir'])
        copy_assets(assets_dir, output_dir, quiet)

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
        '--address',
        default='127.0.0.1',
        help='IP to serve files on.'
    )
    parser.add_argument(
        '--noserver',
        action='store_true',
        help='Don\'t run the server.'
    )
    parser.add_argument(
        '--overwrite',
        default=False,
        action='store_true',
        help='Overwrite the output directory without prompting.'
    )
    parser.add_argument(
        '--watch',
        action='store_true',
        help='Will watch a folder for changes and then process if an event is fired'
    )
    args = parser.parse_args()
    return args

def watching_file_system():
    """ 
    Using watchdog, we'll monitor the filesystem for any changes, and if
    we find any, we'll serve the output again (by running complexity)
    """
    # Get the path we'll need to monitor, it'll be part of the arg list
    args = get_complexity_args()

    # make absolute because server chdirs
    proj_dir = os.path.abspath(args.project_dir)

    # Lets observe the folder, and notify complexity when something bad happens
    observer = Observer()
    event_handler = MyHandler(project_dir=proj_dir)

    for dir_ in ("templates_dir", "macros_dir", "assets_dir", "context_dir"):
        path = _get_dir(proj_dir, dir_)
        print("Watching folder " + path + " for changes:")
        observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # We'll now continue to look until we Ctrl-C finish
    try:
        if args.noserver:
            while True:
                time.sleep(1)
        else:
            output_dir = _get_output_dir(args.project_dir)
            serve_static_site(output_dir=output_dir, address=args.address, port=args.port)
    except KeyboardInterrupt:
        observer.stop();

    observer.join()

"""
This class handles at which points we should process the complexity system again. 
We are targeting any events
"""
class MyHandler(FileSystemEventHandler):

    def __init__(self, project_dir, *args, **kwargs):
        super(MyHandler, self).__init__(*args, **kwargs)
        self._project_dir = project_dir

    def on_any_event(self, event):
        args = get_complexity_args()
        complexity(project_dir=self._project_dir, no_input=False,
                   quiet=True,
                   overwrite=True,
                   _leave_output=True)  # delete contents of www
        print("     [" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "] -> Completed")
        
def main():
    """ Entry point for the package, as defined in `setup.py`. """

    args = get_complexity_args()

    if args.watch == True:
        watching_file_system()
    else:
        output_dir = complexity(project_dir=args.project_dir, overwrite=args.overwrite, no_input=False)
        if not args.noserver:
            serve_static_site(output_dir=output_dir, address=args.address, port=args.port)

if __name__ == '__main__':
    watching_file_system()
