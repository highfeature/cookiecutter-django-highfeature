#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from django import forms
from ..models.project import Project

__author__ = 'Alain Ivars'
logger = logging.getLogger(__name__)


class DetailsReadonlyForm(forms.ModelForm):
    """Gestion formulaire vue de Projet"""
    class Meta:
        """Gestion des données du formulaires de Projet"""
        model = Project
        # select fields and they show order
        fields = (
            'unix_name', 'name', 'short_description', 'homepage', 'is_public',
            'font_awesome', 'image', 'authors',
        )
