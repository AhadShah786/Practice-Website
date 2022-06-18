from email import message
from multiprocessing import context
from re import A
from tkinter import N
from urllib import response
from django import http
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
#from platformdirs import user_cache_path
from  .models import aloochat

# Create your views here.
def index(request):
    aloo = aloochat()
    aloo.name = 'chana chaat'
    aloo.reply = 'fruit chaat'
    aloo.id = 99
    return render(request, 'index.html' , {'aloowala' : aloo}) 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
    
        
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info (request , "This email adress is already taken")
                return redirect ('register')
            elif User.objects.filter(username = username).exists():
                messages.info (request , "This user name is already taken  ")
                return redirect ('register') 
            else:
                user = User.objects.create_user (username = username, email = email, password = password)
                user.save()
                return redirect ('login')
        else:
            messages.info(request , 'Password did not match')
            return redirect ('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
           auth.login(request, user)
           return redirect('/')
        
        else:
            messages.info(request, 'Worng information or credentials') 
            return redirect ('login')
    
    else: 
        
        return render (request , 'login.html')


def counter(request):
        posts = [ 1,2,3,4,'hi','oh']
        return render(request, "counter.html", {"posts" : posts}) 

def post(request, ak):
    return render (request, 'post.html',{'ak' : ak})    
    
    