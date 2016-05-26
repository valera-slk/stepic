from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from qa.views import test

urlpatterns = [
    url(r'^$', 'qa.views.test', name = 'test'),
    url(r'^login/$', 'qa.views.test', name = 'test'),
    url(r'^signup/$', 'qa.views.test', name = 'test'),
    url(r'^question/(\d+)/$', 'qa.views.test', name = 'test'),
    url(r'^ask/.*$', 'qa.views.test', name = 'test'),
    url(r'^popular/$', 'qa.views.test', name = 'test'),
    url(r'^new/$', 'qa.views.test', name = 'test'),
]
