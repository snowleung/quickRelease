#coding:utf-8

import web
from core import appconf
from core.auto_build import AutoBuild
from core.client_down import ClientDown

APPS = AutoBuild([('jinziqi.ipa', 'home.jinziqi'), ('imagesC.ipa', 'home.ImagesC')])
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/(.+)xml', 'ClientDown_handler'
)


class index:
    def GET(self):
        return render.index(APPS.builds)

client_down = ClientDown(APPS.builds)
class ClientDown_handler:
    def GET(self, key):
        web.header('Content-Type', 'text/xml')
        app_conf = client_down.get_config(key)
        return render.appdown(app_conf)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
