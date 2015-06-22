
__author__ = 'Alain Ivars'

from django.conf.urls import patterns, include, url

from contact_form_bootstrap.views import ContactFormView, CompletedPage

from {{cookiecutter.repo_name}}.site.views import index, about, project, mentions


urlpatterns = patterns(
    '',
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^$', index.IndexView.as_view(), name='homepage'),
    url(r'^about$', about.AboutView.as_view(), name='about'),
    url(r'^mentions$', mentions.MentionsView.as_view(), name='mentions'),

    url(r'^contact$', ContactFormView.as_view(), name="contact"),
    url(r'^contact/completed/$', CompletedPage.as_view(), name="completed"),

    url(r'^projects$', project.ProjectsView.as_view(), name='project'),
    url(r'^project/(?P<project_name>[\w-]+)$', project.ProjectShowView.as_view(), name='project_details'),
)

