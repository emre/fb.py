from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    if not request.facebook.is_authenticated():
        return HttpResponseRedirect(request.facebook.get_login_url())
    else:
        user_info = request.facebook.graph().get_object("me")
        return render_to_response("welcome.html", user_info, context_instance = RequestContext(request))

def myfriends(request):
    if request.facebook.is_authenticated():
        print request.facebook.auth_token
        friends = request.facebook.graph().get_object("me/friends")
        for friend in friends["data"]:
            friend["avatar_url"] = request.facebook.graph().get_picture(friend["id"],"small")
        
        return render_to_response("myfriends.html", {"entries": friends["data"]}, context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect(request.facebook.get_login_url())
        
