"""
WSGI config for task_remainder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "task_remainder.settings")

application = get_wsgi_application()

# # for websocket
# from ws4redis.uwsgi_runserver import uWSGIWebsocketServer

# _django_app = get_wsgi_application()
# _websocket_app = uWSGIWebsocketServer()

# def application(environ, start_response):
#     if environ.get('PATH_INFO').startswith(settings.WEBSOCKET_URL):
#         return _websocket_app(environ, start_response)
#     return _django_app(environ, start_response)
