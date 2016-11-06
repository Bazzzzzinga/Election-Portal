from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name='Election_Portal'
urlpatterns=[
			url(r'^$',views.home,name='index'),
			url(r'^OnGoing/$',views.OnGoing,name='OnGoing'),
		    url(r'^election/(?P<pk>\d+)/nominations/$',views.nominations,name='nominations'),
			url(r'^status/$',views.status,name='status'),
			url(r'^past/$',views.past,name='past'),
			url(r'^election/(?P<pk>\d+)/ama/$',views.ama,name='ama'),
			url(r'^aboutupcoming/$',views.aboutupcoming,name='aboutupcoming'),
			url(r'^accounts/login/$', auth_views.login, {'template_name': 'Election_Portal/login.html'},name='login'),
    		url(r'^accounts/logout/$',auth_views.logout,{'next_page': '/'},name='logout'),
 			url(r'^election/(?P<pk>\d+)/vote/$',views.vote,name='vote'),
    		   		
]