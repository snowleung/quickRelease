#coding:utf-8
import unittest
from auto_build import AutoBuild
from appconf import App_iOS_Config

class AutoBuildTest(unittest.TestCase):
    def setUp(self):
        self.abuild = AutoBuild()
    def testBuildList(self):
        self.assertEqual([], self.abuild.builds)

    def testReadfile(self):
        files = ['jinziqi.ipa']
        self.abuild.generateFilesConfig(files)
        self.assertTrue(len(self.abuild.builds) == len(files))

    def testFileConfigClass(self):
        files = ['jinziqi.ipa']
        self.abuild.generateFilesConfig(files)
        jinziqi_ios_config = self.abuild.builds[0]
        self.assertTrue(isinstance(jinziqi_ios_config, App_iOS_Config))

    def testFileConfigTitle(self):
        files = ['jinziqi.ipa']
        self.abuild.generateFilesConfig(files)
        jinziqi_ios_config = self.abuild.builds[0]
        self.assertTrue(jinziqi_ios_config.title == 'jinziqi')

if __name__ == '__main__':
    unittest.main()
