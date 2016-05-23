from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^$', 'qa.views.test'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'^question/(\d+)$', 'qa.views.test'),
    url(r'^ask/.*$', 'qa.views.test'),
    url(r'^popular/$', 'qa.views.test'),
    url(r'^new/$', 'qa.views.test'),
)
