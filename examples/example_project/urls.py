from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from fbconnect.views import index, myfriends, facebook_login_required_view, view_with_no_access, extra_arguments_example

urlpatterns = patterns('',
    # Example:
    # (r'^trailer/', include('trailer.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url('^fbconnect/$', index, name = "index"),
    url('^fbconnect/myfriends$', myfriends, name = "myfriends"),
    url('^no_auth', view_with_no_access, name = "view_with_no_access"),
    url('^login_required/$', facebook_login_required_view, name = "facebook_login_required_view"),
    url('^extra_arguments/$', extra_arguments_example, name = "extra_arguments_example"),
)
