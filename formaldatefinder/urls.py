from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formaldatefinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #/
    url(r'^$', 'formaldatefinder.views.index', name='index'),

    # /admin
    url(r'^admin/', include(admin.site.urls)),

    # /register
    url(r'^register/', 'formaldatefinder.views.register', name='register'),

    # /upcoming
    url(r'^upcoming/', 'formaldatefinder.views.upcoming', name='upcoming'),

    # /event/10
    url(r'^event/(?P<event_id>\d+)/$', 'formaldatefinder.views.event', 
      name='detail'),
)
