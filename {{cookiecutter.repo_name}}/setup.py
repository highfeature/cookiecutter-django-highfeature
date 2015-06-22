#!/usr/bin/python
# ex:set fileencoding=utf-8:

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import {{cookiecutter.repo_name}}

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'argparse==1.2.1',
    'django-crispy-bootstrap==0.1.1.1',
    'django-crispy-forms==1.4.0',
    'django-contactform-bootstrap==0.5.9',
    'django-extra-views==0.6.4',
    'requests==2.7.0',
]

prod_requires = [
    'psycopg2==2.5.2',
    'raven==4.0.4',
]

dev_requires = [
    'flake8>=1.6,<2.0',
    'django-extensions==1.5.5',
    'django-debug-toolbar==1.3.0',
    'raven==4.0.4',
]

tests_require = [
    'pytest',
    'pytest-cov>=1.4',
    'pytest-django',
    'mock',
    'cov-core==1.15.0',
    'coverage==3.7.1',
]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='{{cookiecutter.repo_name}}',
    version={{cookiecutter.repo_name}}.VERSION,
    packages=find_packages('.'),
    include_package_data=True,
    license='BSD License',
    description='A Django Base site form with bootstrap 3 ',
    long_description=README,
    url='http://www.github.com/alainivars/{{cookiecutter.repo_name}}/',
    author='Alain Ivars',
    author_email='alainivars@highfeature.com',
    extras_require={
        'tests': tests_require,
        'dev': dev_requires,
        'prod': prod_requires,
    },
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
