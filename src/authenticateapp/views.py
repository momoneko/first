from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django import forms
from .userform import UserForm
from django.contrib.auth.models import User


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
                return render(
                    request, "login/login.html",
                    {'message': 'Account disabled'}
                    )
        else:
            return render(
                request, "login/login.html",
                {'message': 'Wrong Username/Password'}
                )


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
                )
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            login(request, user)
            return redirect('private2')
    else:
        form = UserForm()
    return render(request, "login/register.html", {
        'form': form,
    })
