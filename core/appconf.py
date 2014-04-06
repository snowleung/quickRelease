#coding:utf-8

class baseConfig:
    def __init__(self):
        self.local_ip = '192.168.11.222'
        self.file_prefix = 'static/client'

class App_iOS_Config(baseConfig):
    def __init__(self):
        baseConfig.__init__(self)
        self.ipa_file = 'noset'
        self.ipa_bundle_id = 'noset'
        self.bundle_version = '0'
        self.subtitle = 'noset'
        self.title = 'noset'
        self.ipa_url = 'http://ip/prefix/file'
        self.ipa_url = self.ipa_url.replace('ip', self.local_ip)
        self.ipa_url = self.ipa_url.replace('prefix', self.file_prefix)
        self.ipa_url = self.ipa_url.replace('file', self.ipa_file)
