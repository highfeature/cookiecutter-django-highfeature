#-*- coding: utf-8 -*-
__author__ = 'Alain Ivars'

import logging

from django import template

logger = logging.getLogger('{{cookiecutter.repo_name}}')

register = template.Library()

@register.inclusion_tag('header.html', takes_context=True)
def nav_header(context, requestor=None):
    logger.debug('context: {0}, requestor: {1}'.format(context, requestor))
    if 'url' in context:
        return {
            'url': context['url'],
            'userName': requestor,
        }
    else:  # for Error pages
        return {
            'userName': requestor,
        }

@register.inclusion_tag('footer.html')
def nav_footer():
    logger.debug('nav_footer')
    return
