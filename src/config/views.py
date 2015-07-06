from django.http import HttpResponse
import random

def helloWorld(request):
    return HttpResponse("Hello World")

def hello(request):
    r = random.randint(0,100)
    return HttpResponse("Hello {0}".format(r))
