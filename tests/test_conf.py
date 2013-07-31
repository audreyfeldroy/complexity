#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_conf
------------

Tests for `complexity.conf` module.
"""

import shutil
import unittest

from complexity import conf


class TestConf(unittest.TestCase):

    def test_read_conf(self):
        conf_dict = conf.read_conf()
        self.assertFalse(conf_dict)
