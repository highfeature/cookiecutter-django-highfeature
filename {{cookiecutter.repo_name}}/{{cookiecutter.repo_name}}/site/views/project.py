#-*- coding: utf-8 -*-

import logging
from django.views import generic
from ..forms.project import DetailsReadonlyForm
from ..models.project import Project

__author__ = 'Alain Ivars'
logger = logging.getLogger(__name__)


class ProjectsView(generic.TemplateView):
    """Gestion de la page vue de projet"""
    template_name = 'project/index.html'

    def get_context_data(self, **kwargs):
        """Gestion du contexte projet"""
        logger.debug('ProjectsView')
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['url'] = 'project'
        context['list_project'] = Project.objects.all()
        return context


class ProjectShowView(generic.UpdateView):
    """Gestion de la page vue de projet"""
    template_name = 'project/details.html'
    slug_field = 'unix_name'
    slug_url_kwarg = 'project_name'
    model = Project
    form_class = DetailsReadonlyForm

    def get_context_data(self, **kwargs):
        """Gestion du contexte projet"""
        logger.debug('ProjectShowView')
        context = super(ProjectShowView, self).get_context_data(**kwargs)
        context['url'] = 'project'
        return context

