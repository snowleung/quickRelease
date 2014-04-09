#coding:utf-8
import unittest
import os
import random
from appconf import App_iOS_Config

class autoBuild():
    def __init__(self, files = None):
        self.builds = []
        if files is not None:
            self.generateFilesConfig(files)
    def generateFilesConfig(self, files):
        for f in files:
            app = App_iOS_Config()
            ipa_file = os.path.split(f)[1]
            ipa_file_name = os.path.splitext(ipa_file)[0]
            app.ipa_file = ipa_file
            app.ipa_bundle_id = str(random.random()*10)[0]
            app.appxmlurl = ipa_file_name
            app.title = ipa_file_name
            self.builds.append(app)
        return len(self.builds)

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
