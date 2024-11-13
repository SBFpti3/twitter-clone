from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CreateUser, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import Data_Serializer
from .models import Data

# Create your views here.

class Home(APIView) :
    def get(self, request) :
        return redirect('homepage')

def signup(request) :
    form = CreateUser()
    if request.method == "POST" :
        form = CreateUser(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    context = {'registerform' : form}
    return render(request, 'twtcloneapp/signup.html', context=context)

def login(request) :
    form = LoginForm()
    if request.method == "POST" :
        form = LoginForm(request, data=request.POST)
        if form.is_valid() :
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None :
                auth.login(request, user)
                return redirect('')
            else :
                messages.error(request, "Wrong username or password.")
        else :
            messages.error(request, "Wrong username or password.")
    context = {'loginform' : form}
    return render(request, 'twtcloneapp/login.html', context=context)

def logout(request) :
    auth.logout(request)
    return redirect('login')

@method_decorator(login_required(login_url='login'), name='dispatch')
class Homepage(APIView) :
    def get(self, request) : 
        return render(request, 'twtcloneapp/index.html')