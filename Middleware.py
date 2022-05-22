from werkzeug.wrappers import Response

class Middleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if True:
            return self.app(environ, start_response)
        res = Response(u'Authorization Failed', mimetype='text/plain', status=401)
        return res(environ, start_response)
