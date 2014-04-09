#coding:utf-8

class ClientDown():
    def __init__(self, configs):
        self.configs = configs
    def get_config(self, key):
        for c in self.configs:
            if key == c.title:
                return c
        return None
