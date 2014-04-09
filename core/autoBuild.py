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
            app = App_iOS_Config(f, str(random.random()*10)[0])
            self.builds.append(app)
        return len(self.builds)

