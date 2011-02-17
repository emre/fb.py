# -*- coding: utf8 -*-

from django.http import HttpResponseRedirect

def require_facebook_login(function):
    """
    login_required decorator for views.
    """
    def wrap(request, *args, **kwargs):
        if not request.facebook.is_authenticated():
            return HttpResponseRedirect(request.facebook.get_login_url())
        return function(request, *args, **kwargs)
    return wrap
