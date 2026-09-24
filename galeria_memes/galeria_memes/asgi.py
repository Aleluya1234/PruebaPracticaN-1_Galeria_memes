"""
ASGI config for galeria_memes project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'galeria_memes.settings')

application = get_asgi_application()
