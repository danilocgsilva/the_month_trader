from werkzeug.wrappers import Response, Request
from flask_login import current_user, login_required
from flask import request

class Middleware:

    def __init__(self, app):
        self.app = app

    #@login_required
    def __call__(self, environ, start_response):
        request = Request(environ)
        request_path = request.path
        if request_path == '/symbol':
            if current_user.is_authenticated:
                message = u"Usuario autenticado"
            else:
                message = u"Usuario não autenticado"
            res = Response(message + request.environ['user']['name'], mimetype='text/plain', status=403)
            return res(environ, start_response)
            if current_user:
                return self.app(environ, start_response)
            else:
                res = Response(u'Authentication Failed', mimetype='text/plain', status=403)
                return res(environ, start_response)
        return self.app(environ, start_response)

        #request = Request(environ)
        #return 'hi'
        #return 'path: %s, url: %s'.format(request.path, request.url)
        #if current_user:
        #    return self.app(environ, start_response)
        #res = Response(u'Authorization Failed', mimetype='text/plain', status=401)
        #res = Response('path: {}, url: {}'.format(request.path, request.url), mimetype='text/plain', status=401)
        #return res(environ, start_response)
