#coding:utf-8
import unittest
from autoBuild import autoBuild
from appconf import App_iOS_Config

class autoBuildtest(unittest.TestCase):
    def testBuildList(self):
        abuild = autoBuild()
        self.assertEqual([], abuild.builds)

    def testReadfile(self):
        abuild = autoBuild()
        files = ['/Users/snow/Desktop/jinziqi.ipa']
        abuild.generateFilesConfig(files)
        self.assertTrue(len(abuild.builds) == len(files))

    def testFileConfigClass(self):
        abuild = autoBuild()
        files = ['/Users/snow/Desktop/jinziqi.ipa']
        abuild.generateFilesConfig(files)
        jinziqi_ios_config = abuild.builds[0]
        self.assertTrue(isinstance(jinziqi_ios_config, App_iOS_Config))

    def testFileConfigTitle(self):
        abuild = autoBuild()
        files = ['/Users/snow/Desktop/jinziqi.ipa']
        abuild.generateFilesConfig(files)
        jinziqi_ios_config = abuild.builds[0]
        self.assertTrue(jinziqi_ios_config.title == 'jinziqi')

if __name__ == '__main__':
    unittest.main()
