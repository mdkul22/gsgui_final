from django.shortcuts import render

# Create your views here.

def login_button(request):
    return render(request, 'loginpage/login_button.html', {})

