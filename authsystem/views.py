from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('dash')
    else:
        return render(request,'login.html')

def dasboard(request):
    return render(request,'success.html')

def logout_user(request):
    logout(request)
    return redirect('login_us')
