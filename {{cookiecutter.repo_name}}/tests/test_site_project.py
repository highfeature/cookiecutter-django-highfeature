from __future__ import unicode_literals

__author__ = 'alainivars'


from django import test
from django.core import serializers
from django.db import models
from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.views.generic import TemplateView

from {{cookiecutter.repo_name}}.site.models.project import Project
from {{cookiecutter.repo_name}}.site.forms.project import DetailsReadonlyForm
from {{cookiecutter.repo_name}}.site.views import index

from mock import Mock

class DetailsReadonlyFormTests(test.TestCase):

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(DetailsReadonlyForm, ModelForm))

class ProjectTests(test.TestCase):

    def test_is_subclass_of(self):
        self.assertTrue(issubclass(Project, models.Model))

    def test_values_json(self):
        p = Project()
        assert serializers.serialize("json", [p], indent=4) == p.values_json()

    def test_str(self):
        p = Project()
        assert '' == str(p)

    def test_authors_as_list(self):
        p = Project()
        assert '' == p.authors_as_list()

