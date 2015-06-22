#-*- coding: utf-8 -*-
"""
This file demonstrates writing tests. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class HomepageTestCase(TestCase):
    #@TODO: Optimiser les données de test pour un run plus rapide
    # fixtures = ['initial_data.json.old']

    def test_basic(self):
        self.client = Client()
        self.client.login(username='admin', password='admin')
        # Issue a GET request.
        response = self.client.get('/')
        self.client.logout()
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['siteName']), 15)
        self.assertEqual(response.context['siteName'], '{{cookiecutter.repo_name}}')

