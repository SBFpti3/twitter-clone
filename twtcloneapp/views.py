from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUser, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

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

@login_required(login_url='login')
def homepage(request) :    
    return render(request, 'twtcloneapp/index.html')