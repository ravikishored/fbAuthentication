from django.conf.urls import patterns, include, url
from facebook import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
       (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),    
     url(r'^', include('ProfileViewer.urls')),
    
    
 #    url(r'^admin/', include(admin.site.urls)),
)
