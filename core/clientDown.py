#coding:utf-8

class ClientDown():
    def __init__(self, configs):
        self.configs = configs
    def get_configs(self, key):
        for c in self.configs:
            if key == c.title:
                return c
        return None
