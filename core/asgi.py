"""
ASGI config for core project.
"""

import os

from django.core.asgi import get_asgi_application

IS_RAILWAY = 'RAILWAY_STATIC_URL' in os.environ  # Railway ke liye environment variable

settings_module = 'core.deployment_settings' if IS_RAILWAY else 'core.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
