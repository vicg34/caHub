"""
WSGI config for thecahub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/CaHub/caHub/thecahub/')
sys.path.append('/home/ubuntu/CaHub/env/bin/python')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thecahub.settings")

application = get_wsgi_application()
