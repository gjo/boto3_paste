# -*- coding: utf-8 -*-

import unittest


class NormalizeConfigTestCase(unittest.TestCase):

    def test(self):
        from .. import normalize_config
        config = {
            'aaa.aws_access_key_id': '__some_key__',
            'aaa.botocore.config_file': '__some_path__',
            'aaa.botocore.credentials_file': '__some_path__',
        }
        kwargs = {
            'botocore.credentials_file': '__some_path_2__',
        }
        ret = normalize_config(config, 'aaa.', **kwargs)
        self.assertDictEqual(ret, {
            'aws_access_key_id': '__some_key__',
            'botocore': {
                'config_file': '__some_path__',
                'credentials_file': '__some_path_2__',
            }
        })
