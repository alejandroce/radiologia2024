# -*- encoding: utf-8 -*-
import json
from .base import *
import os

#ALLOWED_HOSTS = ['*']

# with file(PROJECT_DIR.child("config.json")) as cfg:
#     config = json.load(cfg)

# configuracion de correo
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = config["EMAIL"]["USER"]
# EMAIL_HOST_PASSWORD = config["EMAIL"]["PASSWORD"]
# EMAIL_PORT = 587
#

DEBUG = True

PRIVATE_MEDIA_SERVER = 'private_media.servers.NginxXAccelRedirectServer'

import sentry_sdk
sentry_sdk.init("https://ab73b18401144d0bb21e64b1d1913af6@o419186.ingest.sentry.io/5329634")

# RAVEN_CONFIG = {
#     'dsn': 'https://3c7156731e7c4816bed61f640af69fbc:a358458a3b13429fb7b762a7ddb8860e@sentry.io/130093',
#     # If you are using git, you can also automatically configure the
#     # release based on the git info.
#     'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
# }
#
# INSTALLED_APPS = INSTALLED_APPS + (
#     'raven.contrib.django.raven_compat',
# )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rad2020',
        'USER': 'root',
        'PASSWORD': 'mac3t31',
        'HOST': 'localhost',
        'PORT': '',
    }
}

