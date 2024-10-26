"""
WSGI config for diti_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from core import admin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diti_server.settings')

application = get_wsgi_application()

# Load site configuration
admin.site.reload_settings()
