from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from unclesback import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^users/$', views.test_users, name='user-list')#,
  #  url(r'^login/$', views.authenticate_user, name="authenticate_user")
)

urlpatterns = format_suffix_patterns(urlpatterns)