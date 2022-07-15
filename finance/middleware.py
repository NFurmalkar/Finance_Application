from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect

class VerifyMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request,id=None, *args, **kwargs):
        print("The pre-processing request")
        if not request.session.get('email'):
            #return HttpResponse("<h1>Please Login</h1> <a href="'/#'">Login</a>")
            return HttpResponseRedirect('/')
        if id:
            response = self.get_response(request,id)
            print("the post-processing request")
            return response
        else:
            response = self.get_response(request)
            print("the post-processing request")
            return response

    def process_exception(self, request, exception):  # Fire when view.py get some error

        s1 = "<h1>Application Fetching some Errors</h1>"
        s2 = "<h1>Raised Exception:{}</h1>".format(exception.__class__.__name__)
        s3 = "<h1>Exception: {} </h1>".format(exception)

        return HttpResponse(s1 + s2 + s3)

