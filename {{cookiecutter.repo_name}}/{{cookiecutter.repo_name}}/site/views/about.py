#-*- coding: utf-8 -*-
__author__ = 'Alain Ivars'

from django.views import generic


class AboutView(generic.TemplateView):
    """Gestion de la page about"""
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['url'] = 'about'
        return context

