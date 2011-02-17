# -*- coding: utf8 -*-

import urllib

from fbpy import FBPY

from django.conf import settings

def get_token_from_facebook(code):
    """
    gets auth token for the returned code from Facebook.
    """
    query_string = {
        "client_id"     : settings.FACEBOOK_CONFIG.get("app_id"),
        "redirect_uri"  : settings.FACEBOOK_CONFIG.get("redirect_uri"),
        "client_secret" : settings.FACEBOOK_CONFIG.get("app_secret"),
        "code"          : code,
    }
    content = urllib.urlopen("https://graph.facebook.com/oauth/access_token?%s" % urllib.urlencode(query_string)).read()
    return content

class FBPYMiddleware(object):
    
    def process_request(self, request):
        facebook = getattr('request', 'facebook', None)
        if not facebook:
            request.facebook = FBPY()
            request.facebook.set_config(settings.FACEBOOK_CONFIG)
            if request.session.has_key("token_string"):
                request.facebook.set_token(request.session.get("token_string"))
        """
        if facebook returned back the user session, register it.
        """
        if request.GET.has_key("code"):
            try:
               token_string =  get_token_from_facebook(request.GET.get("code")).split("=")[1]
               request.facebook.set_token(token_string)
               # cache in session
               request.session["token_string"] = token_string
            except Exception, error:
               pass

    def process_response(self, request, response):
        response['P3P'] = 'CP="NOI DSP COR NID ADMa OPTa OUR NOR"'
        return response 
        

