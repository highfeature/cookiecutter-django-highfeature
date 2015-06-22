#-*- coding: utf-8 -*-

# Django settings for Site project.
from .prod import *

DEBUG = TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT = 'static/'
STATIC_URL = 'http://{{cookiecutter.repo_name}}/static/'

ALLOWED_HOSTS += [
    '127.0.0.1', 'localhost',
]

### raven.contrib.django.raven_compat (sentry)
RAVEN_CONFIG = {
    'dsn': 'http://120a79b606944ba8919f7ef390c463c4:15bdcf7f15464d58bf36f5b124ae7cae@sentry:19000/5',
}
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'raven',
)

