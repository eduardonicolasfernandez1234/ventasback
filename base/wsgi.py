"""
WSGI config for base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

application = get_wsgi_application()

User = get_user_model();

# User.objects.create_superuser('admin', 'admin@admin.com', 'password')
