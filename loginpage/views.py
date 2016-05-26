from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as Login
from django.http import HttpResponse, HttpResponseRedirect
from gsgui_final import settings
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                Login(request, user)
                return render(request, 'loginpage/home.html')
            else:
                return render(request, 'loginpage/login.html')
        else:
            return HttpResponseRedirect('loginpage/login.html')
    return render(request, 'loginpage/login.html')
@login_required
def home(request):
	return render(request, 'loginpage/home.html')

