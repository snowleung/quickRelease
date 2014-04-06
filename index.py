#coding:utf-8

import web
from core import appconf

ios_conf = appconf.App_iOS_Config()
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/'+ios_conf.appxmlurl, 'ClientDown_handler'
)


class index:
    def GET(self):
        return render.index(ios_conf)

class ClientDown_handler:
    def GET(self):
        web.header('Content-Type', 'text/xml')
        return render.appdown(ios_conf)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
