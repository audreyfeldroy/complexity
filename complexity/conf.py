#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.conf
-------------------

Functions for reading a `complexity.json` configuration file and doing various
configuration-related things.
"""

import json
import logging
import os

def read_conf(directory):
    """
    Reads and parses the `complexity.json` configuration file from a
    directory, if one is present.
    :param directory: Directory to look for a `complexity.json` file.
    :returns: A conf dict, or False if no `complexity.json` is present.
    """
    
    logging.debug("About to look for a conf file in {0}".format(directory))
    conf_file = os.path.join(directory, 'complexity.json')

    if os.path.isfile(conf_file):
        with open(conf_file) as f:
            conf_dict = json.load(f)
            return conf_dict
    return False
