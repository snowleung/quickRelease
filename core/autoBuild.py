#coding:utf-8
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

