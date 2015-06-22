#-*- coding: utf-8 -*-
__author__ = 'Alain Ivars'

from django.views import generic


class MentionsView(generic.TemplateView):
    """Gestion de la page index"""
    template_name = 'mentions.html'

    def get_context_data(self, **kwargs):
        context = super(MentionsView, self).get_context_data(**kwargs)
        context['url'] = 'homepage'
        return context

