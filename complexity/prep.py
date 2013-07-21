#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

from . import utils


def prompt_and_delete_cruft(output_dir):
    """
    Asks if it's okay to delete output_dir/.
    If so, go ahead and delete it.
    :param output_dir: The Complexity www (output) directory.
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
