"""
WSGI config for core project.
"""

import os

from django.core.wsgi import get_wsgi_application

IS_RAILWAY = 'RAILWAY_STATIC_URL' in os.environ  # Railway ke liye environment variable

settings_module = 'core.deployment_settings' if IS_RAILWAY else 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
