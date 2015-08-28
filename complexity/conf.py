#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
complexity.conf
-------------------

Functions for reading a `complexity.yml` configuration file and doing various
configuration-related things.
"""

import logging
import os
import yaml


def read_conf(directory):
    """
    Reads and parses the `complexity.yml` configuration file from a
    directory, if one is present.
    :param directory: Directory to look for a `complexity.yml` file.
    :returns: A conf dict, or False if no `complexity.yml` is present.
    """

    logging.debug("About to look for a conf file in {0}".format(directory))
    conf_file = os.path.join(directory, 'complexity.yml')

    if os.path.isfile(conf_file):
        with open(conf_file) as f:
            conf_dict = yaml.safe_load(f.read())
            return conf_dict
    return False


def get_unexpanded_list(conf_dict):
    """
    Given a configuration dict, returns the list of templates that were
    specified as unexpanded.
    """

    return conf_dict.get('unexpanded_templates', ())
