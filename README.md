# Build status


[![image](https://api.travis-ci.org/openduty/openduty.svg)](https://travis-ci.org/openduty/openduty)
[![Coverage Status](https://coveralls.io/repos/github/openduty/openduty/badge.svg)](https://coveralls.io/github/openduty/openduty)
[![Requirements Status](https://requires.io/github/openduty/openduty/requirements.svg?branch=master)](https://requires.io/github/openduty/openduty/requirements/?branch=master)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/openduty/opendutyweb)
# What is this?
**Openduty** is an incident escalation tool, just like [Pagerduty](http://pagerduty.com) . It has a Pagerduty compatible API too. 
# Integrations
Has been tested with Nagios, works well for us. Any Pagerduty Notifier using the Pagerduty API should work without a problem.
[Icinga2 config](https://github.com/deathowl/OpenDuty-Icinga2) for openduty integration

# Notifications
Email, SMS, Phone(Thanks Twilio for being awesome!), Push notifications(thanks Pushover, Prowl as well!)and Slack, HipChat, Rocket.chat are supported at the moment.

# Current status
Openduty is in Beta status, it can be considered stable at the moment, however major structural changes can appear anytime (not affecting the API, or the Notifier structure)

# Contribution guidelines
Yes, please. You are welcome.
# Feedback
Any feedback is welcome

# Try it
go to http://demo.openduty.com , log in with root/toor , create your own user.
In heroku demo mode user edit feature is disabled, so you can't misbehave.

# Running on Heroku
add the parts below to your settings.py and add psycopg2==2.5.1 to your requirements.txt

```
# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
# Contributors at Openduty
- [Catalin](https://github.com/catalincoroeanu)
- [deathowl](http://github.com/deathowl)
- [SysRex](https://github.com/sysrex)

# Contributors at Ustream
- [oker](http://github.com/oker1)
- [tyrael](http://github.com/tyrael)
- [dzsubek](https://github.com/dzsubek)
- [ecsy](https://github.com/ecsy)
- [akos](https://github.com/gyim)


# Other contributors
- [DazWorrall](https://github.com/DazWorrall)
- [leventyalcin](https://github.com/leventyalcin)
- [sheran-g](https://github.com/sheran-g)


# Getting started:
```
sudo easy_install pip
sudo pip install pipenv
pipenv install
pipenv shell
export DJANGO_SETTINGS_MODULE=config.settings_dev
docker-compose up
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


because of the `django_tables2` it is tricky to migrate the changes to the DB

One `quick fix` would be to migrate in steps:

First we do:

```bash
./ manage.py migrate notification
```

And the we do:

```bash
./ manage.py migrate openduty
```

Then we can check it by running the general `migrate`

```bash
./ manage.py migrate

```

```bash 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, django_celery_beat, django_twilio, notification, openduty, schedule, sessions
Running migrations:
  No migrations to apply.
(.venv) mac:catalin$ 

```


now, you can start hacking on it.

# Running as a service with systemd
*OpenDuty can be ran as a service with the help of gunicorn and systemd*
```
cp -r systemd/gunicorn.service.* /etc/systemd/system/

cp -r systemd/celery.service* /etc/systemd/system/

// EDIT VARIABLES IN *.service.d/main.conf TO REFLECT YOUR ENV
vi /etc/systemd/system/gunicorn.service.d/main.conf
vi /etc/systemd/system/celery.service.d/main.conf

systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

```

# After you've changed your models please run:
```
./manage.py schemamigration openduty --auto
./manage.py schemamigration notification --auto
./manage.py migrate

```

# If you see a new file appearing in migrations directory when pulling from upstream please run
```
./manage.py migrate
```

# Celery worker:
```
celery -A openduty worker -l info
```

# Login using basic authentication with LDAP-backend

Add the following snippet to your settings_prod/dev.py, dont forget about import

```
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


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
  'openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
)

```


---

# DEMO DATA

1. Migrate
2. `flush` current db content
3. Repopulate `db`



```bash
python manage.py install_demo

```


```bash
Running Migrating on DB.....
Operations to perform:
  Apply all migrations: accounts, admin, auth, contenttypes, django_celery_beat, django_twilio, events, incidents, notification, policies, schedule, schedules, services, sessions
Running migrations:
  No migrations to apply.
Preparing to clear the db.....
All is clean, installing new data...
Installed 52 object(s) from 1 fixture(s)
Successfully installed dummy environment

```



----

### Manual ways

Having `PSQL Docker container` running, you can backup demo sql data:

```bash
pg_dump -h 127.0.0.1 -U openduty --data-only --column-inserts openduty > dummydata.sql

```


Load Demo data:

```bash
pg_dump  -h 127.0.0.1 -U openduty -c --column-inserts openduty < dummydata.sql
```


#### Django way to `Dump Database` and `Load Database`

```bash
python manage.py dumpdata --exclude=contenttypes --exclude=sessions -o demodata.json


```

**Usually `contenttypes` and `sessions` will cause you: **

`IntegrityError: Problem installing fixture 'demodata.json': Could not load     contenttypes.ContentType(pk=2)`


** so we exclude that data since it is not relevant for us anyway.




Load Demo data:

```bash
# Make sure you have a clean DB and  everything migrated
python manage.py fushall

# Load data from demodata.json
python manage.py loaddata demodata.json

```

---
