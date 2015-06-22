__author__ = 'Alain Ivars'

#add this at the end of settings.py if I18N is not working
from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    ".context_processors.site",
    "django.core.context_processors.i18n",
)
