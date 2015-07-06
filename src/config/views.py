from django.http import HttpResponse
import random
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def helloWorld(request):
    return HttpResponse("Hello World")

def hello(request):
    r = random.randint(0,100)
    return HttpResponse("Hello {0}".format(r))
