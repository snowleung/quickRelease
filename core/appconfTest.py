#coding:utf-8
import unittest
import os
from appconf import App_iOS_Config

class appconfTest(unittest.TestCase):
    def test_app_config_init(self):
        ipa_file = 'jinziqi.ipa'
        bundle_id = 1
        ios_conf = App_iOS_Config(ipa_file, bundle_id)
        self.assertTrue(ipa_file == ios_conf.ipa_file)
        self.assertTrue(bundle_id == ios_conf.ipa_bundle_id)
        title = os.path.splitext(ipa_file)[0]
        self.assertTrue(title == ios_conf.title)
        
if __name__ == '__main__':
    unittest.main()
