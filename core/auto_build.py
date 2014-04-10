#coding:utf-8
import os
import random
from appconf import App_iOS_Config

class AutoBuild():
    def __init__(self, files = None):
        self.builds = []
        if files is not None:
            self.generateFilesConfig(files)
    def generateFilesConfig(self, files):
        for f in files:
            app = App_iOS_Config(f[0], f[1])
            self.builds.append(app)
        return len(self.builds)

