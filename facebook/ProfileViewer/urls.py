from django.conf.urls import patterns, include, url

urlpatterns = patterns('ProfileViewer.views',
	

	url(r'^$', 'login', name='login'),
    
  url(r'^get-code$', 'get_code', name='get_code'),

url(r'^get-profile$', 'get_profile', name='get_profile'),
url(r'^get-friends$', 'get_friends', name='get_friends'),
 #   url(r'^upload-resume/$', 'upload', name='upload'),


)
