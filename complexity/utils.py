#!/usr/bin/env python
# -*- coding: utf-8 -*-
import errno
import os
import sys

PY3 = sys.version > '3'
if not PY3:
    import codecs


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return False
    return True


def unicode_open(filename, *args, **kwargs):

    if PY3:
        return open(filename, *args, **kwargs)
    kwargs['encoding'] = "utf-8"
    return codecs.open(filename, *args, **kwargs)