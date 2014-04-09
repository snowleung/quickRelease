#coding:utf-8
import unittest
from appconf import App_iOS_Config
from client_down import ClientDown

class ClientDownTest(unittest.TestCase):
    def setUp(self):
        self.app = App_iOS_Config('jinziqi', '12')
        self.client_down = ClientDown([self.app, ])
    def test_switch_config(self):
        app_config = self.client_down.get_config('jinziqi')
        self.assertTrue(isinstance(app_config, App_iOS_Config))
        self.assertTrue(self.app.title == app_config.title)
    def test_switch_config_not_exists(self):
        app_config = self.client_down.get_config('somethingBreakTheTest')
        self.assertTrue(app_config is None)

if __name__ == '__main__':
    unittest.main()
