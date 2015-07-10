from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm


def log_in(request):
    if request.method == 'GET':
        return render(request, "login/login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                next_page = request.GET.get('next')
                if not next_page:
                    next_page = 'private2'
                return redirect(next_page)
            else:
                return HttpResponse("Account disabled")
        else:
            return render(
                request, "login/login.html",
                {'message': 'Wrong Username/Password'}
                )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('private2')
    else:
        form = UserCreationForm()
    return render(request, "login/register.html", {
        'form': form,
    })
