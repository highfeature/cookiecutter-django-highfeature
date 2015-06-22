#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


def handler400(request):
    context = {
        "errorTitle": _('400 Bad request Error'),
        "errorMsg": _('The 400 Bad Request error is an HTTP status code that means that the request you sent to the website server (e.g. a request to load a web page) was somehow malformed therefore the server was unable to understand or process the request.')
    }
    return render(request, 'error.html', context)


def handler403(request):
    context = {
        "errorTitle": _('403 Forbidden Error'),
        "errorMsg": _('Sorry, but you do not have the right to access to the requested page.')
    }
    return render(request, 'error.html', context)


def handler404(request):
    context = {
        "errorTitle": _('404 Page Not Found Error'),
        "errorMsg": _('The requested resource could not be found but may be available again in the future.')
    }
    return render(request, 'error.html', context)


def handler500(request):
    context = {
        "errorTitle": _('500 Internal Server Error'),
        "errorMsg": _('Sorry, Internal error, please contact your administrator.')
    }
    return render(request, 'error.html', context)
