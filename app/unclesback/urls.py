from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


from unclesback import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^test/(?P<u>[a-z]+/?P<p>[a-z]+)$', views.test, name='test-list'),
    url(r'^signup/$', views.signup_user, name="signup_user")
    url(r'^login/$', views.login_user, name="login_user")
)

urlpatterns = format_suffix_patterns(urlpatterns)