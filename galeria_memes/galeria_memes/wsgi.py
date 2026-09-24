"""
WSGI config for galeria_memes project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galeria_memes.settings')

application = get_wsgi_application()
