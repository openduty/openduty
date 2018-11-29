from config.settings import *

DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
import sys

if 'test' not in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'openduty',
            'USER': 'openduty',
            'PASSWORD': 'secret',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }


BASE_URL = "http://localhost:8000"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devsecret'

PAGINATION_DEFAULT_PAGINATION = 3

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE += [
    # 'apps.openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'