from django.http import HttpResponse
import random

def hello(request):
    r = random.randint(0,100)
    return HttpResponse("Hello {0}".format(r))
