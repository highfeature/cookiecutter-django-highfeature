#-*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from django.core import serializers
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    """Gestion des Projet"""
    #id = models.IntegerField(primary_key=True)
    unix_name = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True, verbose_name=_('Descriptive Project Name'))
    homepage = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Homepage Url'))
    url_doc = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Documentation Url'))
    url_tests = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('Tests Url'))
    is_public = models.BooleanField(default=False)
    for_customer = models.BooleanField(default=False)
    licence = models.CharField(max_length=40, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Short Description'),
                                         help_text=_('255 Character Max, HTML will be stripped from this description'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    font_awesome = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=75, blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'hf_projet'

    def values_json(self):
        return serializers.serialize("json", [self], indent=4)

    def __str__(self):
        return self.unix_name

    def authors_as_list(self):
        return self.authors.split('\n') if self.authors else ''
