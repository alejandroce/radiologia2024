# -*- encoding: utf-8 -*-
"""
    This is the settings file that you use when you're working on the project
    locally. Local development-specific settings include DEBUG mode, log level,
    and activation of developer tools like django-debug-toolbar.
    Developers sometimes name this file dev.py.
    -> @jrperdomoz
"""

from .base import *

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Disable SSLify if DEBUG is enabled.
if DEBUG:
    SSLIFY_DISABLE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rad2020',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# INSTALLED_APPS += ("debug_toolbar", )
"""
INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

MIDDLEWARE_CLASSES += \
    ("debug_toolbar.middleware.DebugToolbarMiddleware", )
"""
WKHTMLTOPDF_CMD  = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
# Set short cache timeout
# CACHE_TIMEOUT = 3600

# '''ARREGLA EL PROBLEMA CON LOS ACENTOS'''
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')