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
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }


BASE_URL = "http://localhost:8000"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devsecret'

PAGINATION_DEFAULT_PAGINATION = 3



#LDAP RELATED
AUTH_LDAP_SERVER_URI = "ldap://fqdn:389"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_START_TLS = False
AUTH_LDAP_MIRROR_GROUPS = True #Mirror LDAP Groups as Django Groups, and populate them as well.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=domain,dc=com",
    ldap.SCOPE_SUBTREE, "(&(objectClass=posixGroup)(cn=openduty*))"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=domain,dc=com",
ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

AUTH_LDAP_USER_ATTR_MAP = {
"first_name": "uid",
"last_name": "sn",
"email": "mail"
}

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE += [
    'apps.openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
