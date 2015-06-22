# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.translation import ugettext_lazy as _


class Migration(migrations.Migration):

    dependencies = [
        # ('{{cookiecutter.repo_name}}', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("unix_name", models.CharField(max_length=40, unique=True)),
                ("name", models.CharField(max_length=64, blank=True, null=True,
                                          verbose_name=_('Descriptive Project Name'))),
                ("homepage", models.CharField(max_length=128, blank=True, null=True,
                                              verbose_name=_('Homepage Url'))),
                ("url_doc", models.CharField(max_length=128, blank=True, null=True,
                                             verbose_name=_('Documentation Url'))),
                ("url_tests", models.CharField(max_length=128, blank=True, null=True,
                                               verbose_name=_('Tests Url'))),
                ("is_public", models.BooleanField(default=False)),
                ("for_customer", models.BooleanField(default=False)),
                ("licence", models.CharField(max_length=40, blank=True, null=True)),
                ("short_description", models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name=_('Short Description'),
                                                       help_text=_('255 Character Max, HTML will be stripped from this description'))),
                ("description", models.TextField(blank=True, null=True, verbose_name=_('Description'))),
                ("font_awesome", models.CharField(max_length=40, blank=True, null=True)),
                ("image", models.CharField(max_length=75, blank=True, null=True)),
                ("authors", models.TextField(blank=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True)),
            ]
        ),
    ]
