from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


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
                return redirect('private')
            else:
                return HttpResponse("Account disabled")
        else:
            return render(
                request, "login/login.html",
                {'message': 'Wrong Username/Password'}
                )
