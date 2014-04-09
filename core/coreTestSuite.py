#coding:utf-8
import unittest
from auto_build_test import AutoBuildTest
from appconf_test import AppconfTest
from client_down_test import ClientDownTest

def suite():
    suites = (
        unittest.makeSuite(AutoBuildTest, "test"),
        unittest.makeSuite(ClientDownTest, "test"),
        unittest.makeSuite(AppconfTest, "test"),
        )
    suite = unittest.TestSuite(suites)
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest = 'suite')
