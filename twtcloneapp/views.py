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
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .serializers import Data_Serializer
from .models import Data

# Create your views here.

class Home(APIView) :
    def get(self, request) :
        return redirect('homepage')

class viewCRUD(APIView) :
    permission = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request) :
        item = Data.objects.all()
        serializer = Data_Serializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) :
        content = request.data.get('content')
        username = request.user.username
        user_instance = request.user.pk
        # return Response({'message': request.user.username}, status=status.HTTP_400_BAD_REQUEST)
        if content :
            serializer = Data_Serializer(data={'content': content, 'username': username, 'user' : user_instance})        
            if serializer.is_valid() :
                serializer.save()
                return redirect('homepage')
            else :
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Content is required!'}, status=status.HTTP_400_BAD_REQUEST)

class viewCRUD2(APIView) :

    permission = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    # untuk put (edit) dan delete belum di handle secara full

    def put(self, request, id) :
        item = get_object_or_404(Data, id = id)        
        serializer = Data_Serializer(item, data = request.data)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id) :
        item = get_object_or_404(Data, id = id)
        
        item.delete()
        return Response({'message' : 'Deleted!'}, status = status.HTTP_200_OK)

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

def user_login(request) :
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

def user_logout(request) :
    auth.logout(request)
    return redirect('login')

@method_decorator(login_required(login_url='login'), name='dispatch')
class Homepage(APIView) :
    def get(self, request) :
        items = Data.objects.all()
        items = list(items)
        items.reverse()
        serializer = Data_Serializer(items, many=True)
        return render(request, 'twtcloneapp/index.html', {'items' : serializer.data})