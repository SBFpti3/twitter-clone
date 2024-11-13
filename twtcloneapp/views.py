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
    
class viewCRUD(APIView) :
    def get(self, request) :
        item = MataKuliah.objects.all()
        serializer = MataKuliah_Serializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = MataKuliah_Serializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class viewCRUD2(APIView) :
    def put(self, request, id) :
        item = get_object_or_404(MataKuliah, id = id)
        serializer = MataKuliah_Serializer(item, data = request.data)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id) :
        item = get_object_or_404(MataKuliah, id = id)
        item.delete()
        return Response({'message' : 'Terhapus!'}, status = status.HTTP_200_OK)

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