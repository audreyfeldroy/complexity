#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.prep
---------------

Functions for preparing a Complexity project for static site generation,
before it actually happens.
"""

import os
import shutil
import glob

from . import utils


def delete_cruft(output_dir, only_contents=False):
    if only_contents:
        print('Deleting {0}/*'.format(output_dir))
        for f in os.listdir(output_dir):
            file_path = os.path.join(output_dir, f)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path, ignore_errors=True)
            except Exception as e:
                print('Error Deleting')
                raise
    else:
        print('Deleting {0}/*'.format(output_dir))
        shutil.rmtree(output_dir, ignore_errors=True)

def prompt_and_delete_cruft(output_dir):
    """
    Asks if it's okay to delete `output_dir/`.
    If so, go ahead and delete it.

    :param output_dir: The Complexity output directory, e.g. `www/`.
    :paramtype output_dir: directory
    """
    if not os.path.exists(output_dir):
        return True

    ok_to_delete = utils.query_yes_no(
        'Is it okay to delete {0}?'.format(output_dir)
    )
    if ok_to_delete:
        shutil.rmtree(output_dir)
        return True
    else:
        print(
            "Aborting. Please manually remove {0} and retry."
            .format(output_dir)
        )
        return False

