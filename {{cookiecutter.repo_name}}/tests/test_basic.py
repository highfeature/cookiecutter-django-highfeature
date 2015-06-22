#-*- coding: utf-8 -*-
"""

This file check basic homepage of this project.
These will pass when you run:
 coverage run --source='.' manage.py test {{cookiecutter.repo_name}}.site.tests.tests_basic.BasicTestCase

"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.utils.translation import ugettext_lazy as _
from django.template.base import Template
from {{cookiecutter.repo_name}} import urls
from {{cookiecutter.repo_name}}.site import views
from {{cookiecutter.repo_name}}.site.views.errors import handler400, handler500


class BasicTestCase(TestCase):
    # fixtures = ['initial_data.json.old']

    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_len_site_name(self):
        response = self.client.get('/')
        self.assertEqual(len(response.context['url']), 8)

    def test_value_site_name(self):
        response = self.client.get('/')
        self.assertEqual(response.context['url'], 'homepage')

    def test_menu_site_name(self):
        response = self.client.get('/')
        self.assertEqual(response.context['url'], 'homepage')

    def test_error400(self):
        self.assertTrue(urls.handler400.endswith('.handler400'))
        factory = RequestFactory()
        request = factory.get('/')
        response = handler400(request)
        #self.assertIn(_('400 Bad request Error'), unicode(response))
        self.assertContains(response, _('400 Bad request Error'))
        #self.assertEqual(response.status_code, 404)

    # def test_error403(self):
    #     self.client.login(username='invite', password='admin')
    #     response = self.client.get(reverse('project_details', kwargs={'project_name': 'project_test'}))
    #     self.assertContains(response, _('403 Forbidden Error'))
    #     self.client.logout()

    def test_error404(self):
        self.client.login(username='invite', password='admin')
        response = self.client.get('/toto')
        self.assertContains(response, _('404 Page Not Found Error'))
        self.client.logout()

    # not work on django 1.6
    def test_project_not_exist(self):
        self.client.login(username='invite', password='admin')
        response = self.client.get(reverse('project_details', kwargs={'project_name': 'project_test'}))
        self.assertContains(response, _('404 Page Not Found Error'))
        self.client.logout()

    def test_error500(self):
        self.assertTrue(urls.handler500.endswith('.handler500'))
        factory = RequestFactory()
        request = factory.get('/')
        response = handler500(request)
        self.assertContains(response, _('500 Internal Server Error'))

    def test_view_about(self):
        response = self.client.get(reverse('about'))
        assert response.status_code == 200

    def test_view_mentions(self):
        response = self.client.get(reverse('mentions'))
        assert response.status_code == 200

    def test_view_project(self):
        response = self.client.get(reverse('project'))
        assert response.status_code == 200

    def test_view_project_details(self):
        response = self.client.get(reverse('project_details', kwargs={'project_name': 'project_test'}))
        assert response.status_code == 200
