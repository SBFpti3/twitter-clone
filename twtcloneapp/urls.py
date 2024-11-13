from django.urls import path
from .views import Homepage, signup, login, logout, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', Homepage.as_view(), name='homepage'),
]
