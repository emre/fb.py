# -*- coding: utf8 -*-

import simplejson

from fbpy import FBPY
from django.conf import settings

class FBPYMiddleware(object):
    
    def process_request(self, request):
        request.facebook = FBPY()
        request.facebook.set_config(settings.FACEBOOK_CONFIG)
        if request.session.has_key("fb_user"):
			if request.session["fb_user"].has_key("access_token"):
				request.facebook.set_token(request.session["fb_user"]["access_token"])
				request.facebook.set_uid(request.session["fb_user"]["uid"])
        """
        if facebook returned back the user session, register it.
        """
        if request.GET.has_key("session"):
            try:
                fb_user = simplejson.loads(request.GET["session"])
                request.session["fb_user"] = fb_user
                request.facebook.set_token(fb_user["access_token"])
            except Exception, error:
				pass

    def process_response(self, request, response):
        response['P3P'] = 'CP="NOI DSP COR NID ADMa OPTa OUR NOR"'
        return response 
    
