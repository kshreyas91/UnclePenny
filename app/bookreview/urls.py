from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from bookreview import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^authors/$', views.test_author, name='author-list'),
    url(r'^login/$', views.authenticate_user, name="authenticate_user")
)

urlpatterns = format_suffix_patterns(urlpatterns)