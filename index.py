#coding:utf-8

import web
from core import appconf
from core.auto_build import AutoBuild

APPS = AutoBuild(['jinziqi.ipa', 'imagesC.ipa'])
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/appxml', 'ClientDown_handler'
)


class index:
    def GET(self):
        return render.index(APPS.builds)

class ClientDown_handler:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        ios_conf = ''
        return render.appdown(ios_conf)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
