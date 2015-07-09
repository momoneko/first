from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def main_page(request):
    return render(request, "main/index.html")


@login_required
def private(request):
    return render(request, "main/private.html")


@login_required
def private2(request):
    return render(request, "main/private2.html")
