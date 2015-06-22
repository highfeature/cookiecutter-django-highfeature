#-*- coding: utf-8 -*-

# Django settings for SiteDJ project.
from .base import *

DEBUG = TEMPLATE_DEBUG = True

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = True

ADMINS = (
    ('Your Name', 'contact@Your.Site'),
)

SITE_FIELD_EMPTY = '-_-_-'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': '{{cookiecutter.repo_name}}',                # Or path to database file if using sqlite3.
    #     # The following settings are not used with sqlite3:
    #     'USER': 'admin',
    #     'PASSWORD': 'admin',
    #     'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
    #     'PORT': '',                      # Set to empty string for default.
    # }
    'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = ['*']

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a dev secret key'

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


### raven.contrib.django.raven_compat (sentry)
RAVEN_CONFIG = {
    'dsn': 'http://120a79b606944ba8919f7ef390c463c4:15bdcf7f15464d58bf36f5b124ae7cae@sentry:19000/5',
}
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'raven',
)


### debug-toolbar
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)

