from django.shortcuts import render, redirect
from django.http import HttpResponse


def main_page(request):
    return render(request, "main/index.html")


def private(request):
    if not request.user.is_authenticated():
        return redirect('log_in')
    else:
        return render(request, "main/private.html")
