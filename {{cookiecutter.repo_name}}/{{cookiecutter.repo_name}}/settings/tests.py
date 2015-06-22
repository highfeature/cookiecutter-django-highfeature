#-*- coding: utf-8 -*-

# Django settings for SiteDJ project.
from .base import *

CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST_NAME': ':memory:',
    },
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SECRET_KEY = 'the-test-key'

# no log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

