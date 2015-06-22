from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

handler400 = '{{cookiecutter.repo_name}}.site.views.errors.handler400'
handler403 = '{{cookiecutter.repo_name}}.site.views.errors.handler403'
handler404 = '{{cookiecutter.repo_name}}.site.views.errors.handler404'
handler500 = '{{cookiecutter.repo_name}}.site.views.errors.handler500'


# class SitemapXml(TemplateView):
#     template_name = "sitemap.xml"
#
#     def render_to_response(self, context, **response_kwargs):
#         response_kwargs['mimetype'] = 'text/plain'
#         return super(SitemapXml, self).render_to_response(context, **response_kwargs)
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(SitemapXml, self).get_context_data(**kwargs)
#         context["DEBUG"] = settings.DEBUG
#         return context

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', '{{cookiecutter.repo_name}}.views.home', name='home'),
    # url(r'^{{cookiecutter.repo_name}}/', include('{{cookiecutter.repo_name}}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # NECESSAIRE pour la traduction
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # NECESSAIRE pour robots.txt, sitemap.xml et favicon.ico
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name="sitemap.xml", content_type='text/plain')),
    # url(r'^sitemap\.xml$', SitemapXml.as_view()),
    # url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/images/favicon.ico'}),

    # Uncomment the next line to enable the admin:
    url(r'^' + settings.ADMIN_URL + '/', include(admin.site.urls)),
    url(r'', include('{{cookiecutter.repo_name}}.site.urls')),
)
