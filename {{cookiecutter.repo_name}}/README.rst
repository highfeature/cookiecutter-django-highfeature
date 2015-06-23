
|Build status| |PyPi version| |PyPi downloads| |Python version| |PyPi wheel| |Project license|

Features
===========================

* Functionality as a django application
  - for an easy integration into an existing django project
  - to make the development of modules easy
  - for the benefit to use a module in an different place of django project (i.e. an online-shop or an customer-interface)
* Login/Logout


Screenshot
===========================

.. image:: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-home.png
   :target: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-home.png
   :alt: Home Screenshot

.. image:: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-about.png
   :target: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-about.png
   :alt: About Screenshot

.. image:: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-contact.png
   :target: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-contact.png
   :alt: Contact Screenshot

.. image:: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-projects.png
   :target: https://github.com/highfeature/cookiecutter-django-highfeature/raw/dev/%7B%7Bcookiecutter.repo_name%7D%7D/docs/static/django-highfeature-projects.png
   :alt: Projects Screenshot

Use
===========================

    + Add in your setting file::

        ADMINS = (
            ('your admin name', 'contact@yourdomain.com'),
        )

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

        CRISPY_TEMPLATE_PACK = 'bootstrap3'

        # your google counter ID
        UA_YOUR = 'UA-you'

    + Don't forget to set::

        EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER and EMAIL_HOST_PASSWORD


    + Be sure to have::

        'homepage' defined in your url file


Documentation
===========================

.. note::
    Please note that this Project is documented poorly. If you have any questions please contact us!
    We'd love to update the documentation and answer your question!

http://www.{{cookiecutter.repo_name}}.com/docs/dev

Demo
===========================

http://demo.{{cookiecutter.repo_name}}.com/

Todo
===========================

 - finish english translation
 - improve coverage
 - clean the theme
 - improve log

Getting Help
===========================

Please report bugs or ask questions using the `Issue Tracker`_ or contact us via team@{{cookiecutter.repo_name}}.com

Check also for the latest updates of this project on Github_.

Credits
===========================

* `django`_
* `django_contactform_bootstrap`_

.. _Github: https://github.com/django-sme/django-{{cookiecutter.repo_name}}
.. _Issue Tracker: https://github.com/django-sme/django-{{cookiecutter.repo_name}}/issues
.. _django: http://www.djangoproject.com
.. _django_contactform_bootstrap: https://github.com/alainivars/django-contact-form

.. |Build status| image:: https://api.travis-ci.org/django-{{cookiecutter.repo_name}}/django-{{cookiecutter.repo_name}}.svg?branch=develop
   :target: http://travis-ci.org/alainivars/django-{{cookiecutter.repo_name}}
.. |PyPi version| image:: https://pypip.in/v/django-bmf/badge.svg?text=version
   :target: https://pypi.python.org/pypi/django-{{cookiecutter.repo_name}}/
.. |PyPi downloads| image:: https://pypip.in/d/django-{{cookiecutter.repo_name}}/badge.svg?period=month
   :target: https://pypi.python.org/pypi/django-{{cookiecutter.repo_name}}/
.. |Python version| image:: https://pypip.in/py_versions/django-{{cookiecutter.repo_name}}/badge.svg
   :target: https://pypi.python.org/pypi/django-{{cookiecutter.repo_name}}/
.. |PyPi wheel| image:: https://pypip.in/wheel/django-{{cookiecutter.repo_name}}/badge.svg
   :target: https://pypi.python.org/pypi/django-{{cookiecutter.repo_name}}/
.. |Project license| image:: https://pypip.in/license/django-{{cookiecutter.repo_name}}/badge.svg
   :target: https://pypi.python.org/pypi/django-{{cookiecutter.repo_name}}/
