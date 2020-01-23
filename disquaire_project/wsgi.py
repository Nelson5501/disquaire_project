"""
WSGI config for disquaire_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys


from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/NelsonCaterino/Documents/Site/learning/Django/disquaire_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'disquaire_project.settings')

application = get_wsgi_application()

