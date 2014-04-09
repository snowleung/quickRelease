#coding:utf-8
import unittest
from appconf import App_iOS_Config
from clientDown import ClientDown

class ClientDowntest(unittest.TestCase):
    def test_switch_config(self):
        a = App_iOS_Config()
        a.title = 'jinziqi'
        c = ClientDown([a, ])
        app_config = c.get_config('jinziqi')
        self.assertTrue(isinstance(app_config, App_iOS_Config))
        self.assertTrue(a.title == app_config.title)

if __name__ == '__main__':
    unittest.main()
