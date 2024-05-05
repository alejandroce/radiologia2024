# -*- encoding: utf-8 -*-
import os
from unipath import Path
import sys

PROJECT_DIR = Path(__file__).ancestor(2)
sys.path.append(PROJECT_DIR.child("radiologia2020"))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Tijuana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.htmlssssssszz
LANGUAGE_CODE = 'en-us'


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

# MEDIA_ROOT = os.path.join(RUTA_PROYECTO, os.pardir, "media")
MEDIA_ROOT = PROJECT_DIR.child("media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

PRIVATE_MEDIA_URL = MEDIA_URL
PRIVATE_MEDIA_ROOT = MEDIA_ROOT
PRIVATE_MEDIA_SERVER = 'private_media.servers.DefaultServer'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = PROJECT_DIR.child("static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR.child("estaticos"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'j7#r7lv=__32qy3alrgc24my06!n-1t+qs2n6%=@873qaslba4'


MIDDLEWARE_CLASSES = (
    # 'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
    # Simple history middleware
   # 'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'radiologia.urls'

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'radiologia.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child("templates")],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                # Default items.
                "django.contrib.auth.context_processors.auth",
                # "django.auth.core.context_processors.auth",
                "django.core.context_processors.debug",
                "django.core.context_processors.i18n",
                "django.core.context_processors.media",
                # Needs to be added for django-staticfiles to allow you to use
                # {{ STATIC_URL }}myapp/my.css in your templates.
                # 'staticfiles.context_processors.static_url',
                "django.core.context_processors.static",
                "django.core.context_processors.tz",
                "django.core.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],

            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ]
        },
    },
]

# APPs CONFIGURATION
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'crispy_forms',
    'django_summernote',
    'pacientes',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# 20MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520

EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_HOST_USER = '7eeb583b90f4c25f4897fd3666f58c44'
EMAIL_HOST_PASSWORD = '6cd6ed834127a2a56b96aa0c35e9da6d'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 8 
PASSWORD_COMPLEXITY = {
    # You can ommit any or all of these for no limit for that particular set
    "UPPER": 1,       # Uppercase
    "LOWER": 1,       # Lowercase
    "DIGITS": 1,      # Digits
    "PUNCTUATION": 0,  # Punctuation (string.punctuation)
    "NON ASCII": 0,   # Non Ascii (ord() >= 128)
    "WORDS": 0        # Words (substrings seperates by a whitespace)
}

USE_THOUSAND_SEPARATOR = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

'''ARREGLA EL PROBLEMA CON LOS ACENTOS'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
