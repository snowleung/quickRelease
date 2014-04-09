#coding:utf-8

import web
from core import appconf
from core.autoBuild import autoBuild

ios_conf = appconf.App_iOS_Config()
APPS = autoBuild(['jinziqi.ipa', 'imagesC.ipa'])
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
        return render.appdown(ios_conf)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
