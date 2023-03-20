from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.models import Place
from.models import team
# Create your views here.


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        secondname=request.POST['second_name']
        email= request.POST['email']
        password= request.POST['password']
        cpassowrd=request.POST['password2']


        user=User.objects.create_user(username=username,first_name=first_name,last_name=secondname,email=email,password=password,cpassowrd=cpassowrd)
        user.save();

        return redirect('login')
        return render(request,"register.html")


