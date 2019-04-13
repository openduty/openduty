import os
import sys
import logging.config
import environ


root = environ.Path(__file__) - 3  # three folder back (/project/config/settings/ - 3 = /)
env = environ.Env()
environ.Env.read_env()

ROOT = root

BASE_DIR = ROOT

ENV = env.str('ENV', default='live')

DEBUG = env.bool('DEBUG', default=False)

TEMPLATE_DEBUG = env.bool('TEMPLATE_DEBUG', default=False)

SECRET_KEY = env('SECRET_KEY', default='@kf^hqfr00#h+jse&37pw0)pr4-@o+xjq0k(-oh)r5@at7sx4u')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='openduty.com')
PREPEND_WWW = env.bool('PREPEND_WWW', default=True)
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
BASE_URL = env('BASE_URL', default='https://www.openduty.com')
HOST = env('HOST', default='www.openduty.com')

# Application definition
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

PROFILE_MODULE = 'apps.accounts.Profile'

AUTH_PROFILE_MODULE = 'apps.accounts.Profile'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'rest_framework',
    'django_celery_beat',
    'django_tables2',
    'django_tables2_simplefilter',
    "django_twilio",
    'schedule',
    'django_admin_generator',

    # Local apps
    'apps.accounts',
    'apps.commons',
    'apps.events',
    'apps.incidents',
    'apps.notification',
    'apps.openduty',
    'apps.opsweekly',
    'apps.policies',
    'apps.schedules',
    'apps.services',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(str(root), "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgresql://openduty:secret@openduty:5432/openduty')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if ENV == 'local':
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logfile',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'celery.log',
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'django.server': {
            'handlers': ['console', 'logfile'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'apps.accounts': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.events': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.incidents': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.notification': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.openduty': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.opsweekly': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.policies': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.schedules': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'apps.services': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)


# *******   EXTRA DJANGO CONFIG ***** #
#######################################

FIRST_DAY_OF_WEEK = 1

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGINATE_BY': 10
}

PAGINATION_DEFAULT_PAGINATION = 20  # The default amount of items to show on a page if no number is specified.

# EMAIL

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', default='mail.openduty.com')
EMAIL_PORT = env('EMAIL_PORT', default=587)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='notification@openduty.com')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='secret')
EMAIL_HOST_NAME = env('EMAIL_HOST_NAME', default='Notification Center')
EMAIL_SENDER_NAME = env('EMAIL_SENDER_NAME', default='Notifications<notification@openduty.com>')
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=False)
EMAIL_USE_SSL = env('EMAIL_USE_SSL', default=False)


TWILIO_SETTINGS = {
    'SID': env('TWILIO_SETTINGS_SID', default=""),
    'token': env('TWILIO_SETTINGS_TOKEN', default=""),
    'phone_number': env('TWILIO_SETTINGS_PHONE_NUMBER', default=""),
    'sms_number': env('TWILIO_SETTINGS_SMS_NUMBER', default=""),
    'twiml_url': env('TWILIO_SETTINGS_TWIM_URL', default="")
}

SLACK_SETTINGS = {
    'apikey': env('SLACK_SETTINGS_APIKEY', default="")
}

PROWL_SETTINGS = {
}

XMPP_SETTINGS = {
}

HIPCHAT_SETTINGS = {
    'token': '',
    'endpoint': ''
}

TWILIO_ACCOUNT_SID = TWILIO_SETTINGS.get("SID", "disabled")

TWILIO_AUTH_TOKEN = TWILIO_SETTINGS.get("token", "disabled")

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


if ENV == 'local':
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_extensions',
    ]
    try:
        from .dev import *
    except ImportError:
        pass


if ENV == 'test':
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
