#coding:utf-8
import os
class baseConfig:
    def __init__(self):
        self.local_ip = '192.168.11.222'
        self.file_prefix = 'static/client'

class App_iOS_Config(baseConfig):
    def __init__(self, ipa_file, bundle_id):
        baseConfig.__init__(self)
        self.ipa_file = ipa_file
        self.ipa_bundle_id = bundle_id
        self.title = os.path.splitext(self.ipa_file)[0]
        self.services_url = 'http://ip/appxml'
        self.services_url = self.services_url.replace('ip', self.local_ip)
        self.services_url = self.services_url.replace('app', self.title)
        self.bundle_version = '1.0'
        self.subtitle = 'notset'
        self.ipa_url = 'http://ip/prefix/file'
        self.ipa_url = self.ipa_url.replace('ip', self.local_ip)
        self.ipa_url = self.ipa_url.replace('prefix', self.file_prefix)
        self.ipa_url = self.ipa_url.replace('file', self.ipa_file)
