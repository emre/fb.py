# -*- coding: utf8 -*-

from django.http import HttpResponseRedirect

"""
login_required decorator for views.
"""
def require_facebook_login(function):
    def wrap(request, *args, **kwargs):
        if request.facebook.is_authenticated() == False:
            return HttpResponseRedirect(request.facebook.get_login_url())
        return function(request, *args, **kwargs)
    return wrap
