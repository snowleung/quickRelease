#coding:utf-8

import web
from core import appconf

urls = (
    '/', 'index',
    '/app', 'ClientDown_handler'
)

render = web.template.render('templates/')

ios_conf = appconf.App_iOS_Config()

class index:
    def GET(self):
        return render.index()

class ClientDown_handler:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        return render.appdown(ios_conf)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
