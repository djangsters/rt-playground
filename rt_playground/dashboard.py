import os

from rt_dashboard.web import app as rt_app
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request


def application(environ, start_response):
    request = Request(environ)
    response = rt_app.get_response('a', request.path, method=request.method)
    return response(environ, start_response)


if __name__ == '__main__':
    host = os.environ.get("HOST", "localhost")
    port = int(os.environ.get("PORT", 8080))
    user_reloader = bool(os.environ.get("USE_RELOADER", True))
    run_simple(host, port, application, use_reloader=use_reloader)
