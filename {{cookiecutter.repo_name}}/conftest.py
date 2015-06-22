__author__ = 'Alain Ivars'

"""
lauch tests by: py.test
with coverage:  py.test --cov-config .coveragerc --cov-report html --cov {{cookiecutter.repo_name}}
old with coverage:  PYTHONPATH=`pwd` py.test --cov-config .coveragerc --cov-report html --cov {{cookiecutter.repo_name}} --ds={{cookiecutter.repo_name}}.settings.tests
"""


def pytest_configure(config):
    from django.conf import settings
    if not settings.configured:
        from {{cookiecutter.repo_name}}.settings import tests as test_settings
        settings.configure(**test_settings.__dict__)

    if not hasattr(settings, 'CACHES'):  # pragma: no cover
        settings.CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            }
        }
    settings.SITE_NAME = '{{cookiecutter.repo_name}}'
    import django
    if django.VERSION[1] >= 7:
        django.setup()

