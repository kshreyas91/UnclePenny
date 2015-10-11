from django.conf.urls import patterns, url

from rest_framework.urlpatterns import format_suffix_patterns


from unclesback import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index_view, name='index_view'),
    url(r'^test/(?P<u>[a-z]+/?P<p>[a-z]+)$', views.test, name='test-list'),
    url(r'^signup/$', views.signup_user, name="signup_user"),
    url(r'^login/$', views.login_user, name="login_user"),
    url(r'^addChallenge/$', views.addNewChallege, name="add_challege"),
    url(r'^listSingleChallenges/$', views.listSingleChallenge, name="list_single"),
    url(r'^listGroupChallenge/$', views.listGroupChallege, name="list_group"),
    url(r'^addNewTeam/$', views.addNewTeam, name="team_add"),
    url(r'^listTeams/$', views.listAllTeamForChallenge, name="list_teams"),
	url(r'^enrollIndividually/$', views.enrollSingleChallenge, name="list_teams"),
	url(r'^enrollWithTeam/$', views.joinTeam, name="enroll_ind"),
	url(r'^getCurrentChallenge/$', views.getUsersCurrentChallenge, name="currentChallenge"),
)

urlpatterns = format_suffix_patterns(urlpatterns)