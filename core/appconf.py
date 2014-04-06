#coding:utf-8

class baseConfig:
    def __init__(self):
        self.local_ip = 'notset'
        self.file_prefix = 'static/client'

class App_iOS_Config(baseConfig):
    def __init__(self):
        baseConfig.__init__(self)
        self.ipa_file = 'notset'
        self.ipa_bundle_id = 'notset'
        self.services_url = 'http://ip/appxmlurl'
        self.appxmlurl = 'app'
        self.services_url = self.services_url.replace('ip', self.local_ip)
        self.services_url = self.services_url.replace('appxmlurl', self.appxmlurl)
        self.bundle_version = '0'
        self.subtitle = 'notset'
        self.title = 'notset'
        self.ipa_url = 'http://ip/prefix/file'
        self.ipa_url = self.ipa_url.replace('ip', self.local_ip)
        self.ipa_url = self.ipa_url.replace('prefix', self.file_prefix)
        self.ipa_url = self.ipa_url.replace('file', self.ipa_file)
