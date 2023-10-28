from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, logout

def register(request):
    return render(request, 'register.html')
def login(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'login.html')

def verify(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("exampleInputUsername1")
        email = login_data.get("exampleInputEmail1")
        phone = login_data.get("exampleInputPhone1")
        password = request.POST.get("inputPassword", False)
        user_type = login_data.get("exampleCheck1")
        data = {
            "username" : username,
            "password" : password,
            "user_type" : user_type,
            "email" : email,
            "phone" : phone,
        }
        print(data)
        
        if username and email and phone and password:
            print(111111111111111111111111111111111)
            user = User.objects.create_user(username,
            email,
            password)
            user.save()
            return render(request, 'index.html')
        else:
            return redirect('/login/register/')


    
def documents(request):
    return render(request, 'document.html')