from django.shortcuts import render,redirect
from django import views
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    return render(request,'login.html')

def registeration(request):

    if request.method == 'POST':
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        password = request.POST['password']

        user=User.objects.create_user(username=Username,email=email,password=password,)
        user.save()
        print('user created')
        return redirect('index.html')


    else:
        return render(request,'registration.html')
