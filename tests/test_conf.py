#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_conf
------------

Tests for `complexity.conf` module.
"""

import logging
import unittest

from complexity import conf


# Log debug and above to console
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class TestConf(unittest.TestCase):

    def test_read_conf(self):
        conf_dict = conf.read_conf('tests/conf_proj')
        logging.debug("read_conf returned {0}".format(conf_dict))
        self.assertTrue(conf_dict)
        self.assertEqual(
            conf_dict,
            {
                'output_dir': '../www',
                'templates_dir': 'templates',
                'unexpanded_templates': ['404.html', '500.html']
            }
        )

    def test_get_unexpanded_list(self):
        conf_dict = {
            'output_dir': '../www',
            'templates_dir': 'templates',
            'unexpanded_templates': ['404.html', '500.html']
        }
        self.assertEqual(
            conf.get_unexpanded_list(conf_dict),
            ['404.html', '500.html']
        )


if __name__ == '__main__':
    unittest.main()
