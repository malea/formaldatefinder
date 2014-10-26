from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'formaldatefinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'formaldatefinder.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'formaldatefinder.views.register', name='register'),
    url(r'^upcoming/', 'formaldatefinder.views.upcoming', name='upcoming'),
)
