#-*- coding: utf-8 -*-

# Django settings for SiteDJ project.
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# default prod
DEBUG = TEMPLATE_DEBUG = False
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '127.0.0.1'
SESSION_COOKIE_SECURE = True

ADMINS = (
    ('Alain Ivars', 'contact@{{cookiecutter.repo_name}}.com'),
)

SITE_FIELD_EMPTY = '-----'
# django admin
SITE_ID = 1

"""The name displayed of the site"""
SITE_URL = 'http://localhost:9000/'

# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'
#DATETIME_INPUT_FORMATS = '%Y-%m-%d %H:%M:%S'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# pour internationalisation d apres le tuto django du site
# http://fr.openclassrooms.com/informatique/cours/developpez-votre-site-web-avec-le-framework-django/qu-est-ce-que-le-i18n-et-comment-s-en-servir
gettext = lambda x: x
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
)

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# valeur par default si pas de next=
LOGIN_REDIRECT_URL = '/'
# url de login
LOGIN_URL = '/login'

# Additional locations of static files
settings_path = os.path.abspath(os.path.dirname(__file__)+'/..')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(settings_path, 'theme/modern-business/'),
    os.path.join(settings_path, 'theme/modern-business/font-awesome/'),
    os.path.join(settings_path, 'theme/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'the base key here'

# List of callables that know how to import templatetags from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware', # 1.7.2
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
if django.VERSION[1] >= 8:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
        'django.middleware.security.SecurityMiddleware',
    )
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    # authentification on all pages
    # '{{cookiecutter.repo_name}}.authentification.middleware.LoginRequiredMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.csrf",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    '{{cookiecutter.repo_name}}.context_processors.right_user',
)

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templatetags".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ( os.path.join(settings_path, 'templates'), )
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next lines to enable the admin:
    'django.contrib.admin',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{{cookiecutter.repo_name}}.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'custom',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['logfile'],
            'level': 'INFO',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s  %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'custom': {
            'format': '%(levelname)s %(asctime)s - %(module)s %(filename)s:%(lineno)d %(funcName)s : %(message)s'
        },
    },
}

### cripy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'crispy_forms',
)

### contact_form_bootstrap
COMPANY = {
    'NAME': "my company",
    'ADDRESS': "26 streets from here th there",
    'ZIP': "1234",
    'CITY': "Maybe-there",
    'LAT': 48.81484460000001,
    'LNG': 2.0523723999999675,
    'PHONE': "+336 1234 5678",
    'EMAIL': 'contact@yourdomain.com',
    'FACEBOOK': "Maybe-there",
    'LINKEDIN': "Maybe-there",
    'TWITTER': "Maybe-there",
    'GOOGLEPLUS': "+Maybe-there",
}
# your google counter ID
UA_YOUR = 'UA-you'


### {{cookiecutter.repo_name}}
"""The name displayed of the site"""
SITE_NAME = '{{cookiecutter.repo_name}}'
ADMIN_URL = 'admin'
#update INSTALLED_APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'contact_form_bootstrap',
    '{{cookiecutter.repo_name}}',
    '{{cookiecutter.repo_name}}.navigation',
    '{{cookiecutter.repo_name}}.site',
)
