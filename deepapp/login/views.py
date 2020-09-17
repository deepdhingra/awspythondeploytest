from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def loginpage(request):
    return render(request,'loginpage.html',{'link3':'http://127.0.0.1:8000/anywebpage'})

def about(request):
    return HttpResponse("<h1>hi this is created by deep dhingra</h1>")

def entered(request):
    return HttpResponse("<h1>deep dhingra welcomes you</h1>")

def anywebpage(request):
    return HttpResponse("<h1>yaha wese hi link h ki bina login kre kisi webpage pr jana h toh</h1>")

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        x = User.objects.create_user(username = username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        return redirect('login page')

    else:
        return render(request,'signuppage.html')

def login(request):
    if request.method =='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        print(username1,password1)
        # from django.contrib import auth
        x = auth.authenticate(username = username1,password = password1)
        if x is None:
            return redirect('login page')
        else:
            return redirect('entered')
    else:
        return render(request,'loginpage.html')