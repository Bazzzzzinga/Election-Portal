from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
app_name='Election_Portal'
urlpatterns=[url(r'^$',views.index,name='index'),
			url(r'^home/$',views.home,name='home'),
			url(r'^OnGoing/$',views.OnGoing,name='OnGoing'),
		        url(r'^nominations/$',views.nominations,name='nominations'),
			url(r'^status/$',views.status,name='status'),
			url(r'^past/$',views.past,name='past'),
			url(r'^ama/$',views.ama,name='ama')
]
