#-*- coding: utf-8 -*-

# Django settings for Site project.
from .base import *

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{cookiecutter.repo_name}}',                # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'your user postgres',
        'PASSWORD': 'your passwword postres',
        'HOST': 'localhost',             # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_ROOT = '../static/'
STATIC_URL = 'http://www.{{cookiecutter.repo_name}}.com/static/'

ALLOWED_HOSTS = [
    '.{{cookiecutter.repo_name}}.com', # Allow domain and subdomains
    '.{{cookiecutter.repo_name}}.com.', # Also allow FQDN and subdomains
]

### raven.contrib.django.raven_compat (sentry)
RAVEN_CONFIG = {
    'dsn': 'http://120a79b606944ba8919f7ef390c463c4:15bdcf7f15464d58bf36f5b124ae7cae@sentry:19000/5',
}
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'raven',
)

