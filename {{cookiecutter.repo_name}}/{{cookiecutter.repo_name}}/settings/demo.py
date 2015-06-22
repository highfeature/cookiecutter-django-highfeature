#-*- coding: utf-8 -*-

# Django settings for Site project.
from .base import *

DEBUG = TEMPLATE_DEBUG = False
DATABASE_NAME = 'django-base-demo'
DATABASE_USER = 'djb_demo'
DATABASE_PASSWORD = 'djb_demo'

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

