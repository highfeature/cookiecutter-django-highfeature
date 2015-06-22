# -*- coding: utf-8 -*-

__author__ = 'Alain Ivars'

import logging

from django.conf import settings

logger = logging.getLogger(__name__)


def right_user(request):
    """Gestion du contexte global pour les droits de l'utilisateur"""
    logger.debug('right_user')
    if not hasattr(request, 'user') or not request.user.is_authenticated():
        return {
            'siteName': settings.SITE_NAME,
            'projectsList': {},
            'userName': '',
            'admin_site': False,
            'super_user': False,
            'projects': {},
            'roles': (),
            'projectsRoles': {},
        }
    admin_site = request.user.is_staff()
    return {
        'siteName': settings.SITE_NAME,
        'projectsList': {},
        'userName': request.user.username,
        'admin_site': admin_site,
        'super_user': admin_site,
        'projects': {},
        'roles': (),
        'projectsRoles': {},
    }
