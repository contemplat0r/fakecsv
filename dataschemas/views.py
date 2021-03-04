from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        pass
        # Return an 'invalid login' error message.
    return

def logout_view(request):
    logout(request)