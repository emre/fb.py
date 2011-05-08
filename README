THIS PROJECT IS NOT MAINTAINED ANYMORE.
=================
thanks for all the feedback in the past.

README

fb.py 
=================

fb.py is a software development kit for Facebook. It supports both old rest api
and new graph api. it uses oauth, old style signature/secretkey based api calls 
for old rest api are not supported at this time. 

you can find official documentation at facebook about api calls and methods.

1) old rest api: http://developers.facebook.com/docs/reference/rest/
2) graph api: http://graph.facebook.com

dependencies
=================
1) python-simplejson

installation
=================

1) get the archive.
2) run python setup.py install (with root priviliges)

usage in Django
=================

1) add these lines to your settings.py  

    FACEBOOK_CONFIG = {
        "redirect_uri"     : "%s/fbconnect" % BASE_URL,
        "scope"            : 'email,publish_stream,offline_access,user_hometown,user_location',
        "api_key"          : "[INSERT_API_KEY_HERE]",
        "app_secret"       : "[INSERT_APPLICATION_SECRET_HERE]",
        "app_id"           : "[INSERT_APPLICATION_ID_HERE]",
    }

2) add to your MIDDLEWARE_CLASSES:

    fbpy.middleware.FBPYMiddleware

    
5) after these steps, you can call FBPY instance as request.facebook. a simple view example: 

    if not request.facebook.is_authenticated():
        return HttpResponseRedirect(request.facebook.get_login_url())
    else:
        user_info = request.facebook.graph().get_object("me")
        return render_to_response("welcome.html", user_info, context_instance = RequestContext(request))
      

6) read the code/wait for more documentation. fb.py is one python file with inline documentation, so browsing the code is a good idea than waiting a fully documentation.

installation of "example_project"
=================

1) there is a sandbox django project in example_project directory.

2) download it and edit settings.py. (FACEBOOK_CONFIG variable.)

3) run python manage.py syncdb (we need sessions!)

4) run python manage.py runserver

5) go to your web browser, and see 127.0.0.1:8000/fbconnect


low level api
=================
        
1) in order to send calls to new graph api, a simple request should be like that:
    reply = request.facebook.graph().get_object("me") 

2) old rest api example: (taking mutual friends for a spesific profile id)
    reply = request.facebook.rest().get_object("friends.getMutualFriends", target_uid = profile_id)

3) happy hacking!
    
to-do
=================

1) more documentation.

2) handling cookie/session storage in FBPY. 

thanks
=================

1) Rabia Sozkesen - for the fantastic name of the library.

2) Timu Eren & Yilmaz Ugurlu - suggestions and ideas.
