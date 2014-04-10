#coding:utf-8
import unittest
from auto_build import AutoBuild
from appconf import App_iOS_Config

class AutoBuildTest(unittest.TestCase):
    def setUp(self):
        self.abuild = AutoBuild()
        self.files = [('jinziqi.ipa', 'home.jinziqi')]
    def testBuildList(self):
        self.assertEqual([], self.abuild.builds)

    def testReadfile(self):
        self.abuild.generateFilesConfig(self.files)
        self.assertTrue(len(self.abuild.builds) == len(self.files))

    def testFileConfigClass(self):
        self.abuild.generateFilesConfig(self.files)
        jinziqi_ios_config = self.abuild.builds[0]
        self.assertTrue(isinstance(jinziqi_ios_config, App_iOS_Config))

    def testFileConfigTitle(self):
        self.abuild.generateFilesConfig(self.files)
        jinziqi_ios_config = self.abuild.builds[0]
        self.assertTrue(jinziqi_ios_config.title == 'jinziqi')

if __name__ == '__main__':
    unittest.main()
