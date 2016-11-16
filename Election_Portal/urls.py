from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name='Election_Portal'
urlpatterns=[
			url(r'^$',views.home,name='index'),
		    url(r'^election/(?P<pk>\d+)/nominations/$',views.nominations,name='nominations'),
		    url(r'^election/(?P<pk>\d+)/nomination_filled/$',views.nomination_filled,name='nomination_filled'),
			url(r'^ama/(?P<pk>\d+)/$',views.ama,name='ama'),
			url(r'^accounts/login/$', auth_views.login, {'template_name': 'Election_Portal/login.html'},name='login'),
    		url(r'^accounts/logout/$',auth_views.logout,{'next_page': '/'},name='logout'),
 			url(r'^election/(?P<pk>\d+)/vote/$',views.vote,name='vote'),
 			url(r'^election/(?P<pk>\d+)/vote_done/$',views.vote_done,name='vote_done'),
 			url(r'^ama/(?P<pk>\d+)/post_comment/$',views.post_comment,name='post_comment'),
 			url(r'^faq/',views.faq,name='faq'),
 			url(r'^contact',views.contact,name='contact'),
 			url(r'^msgsent',views.msgsent,name='msgsent'),
]