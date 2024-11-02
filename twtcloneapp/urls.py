from django.urls import path
from .views import homepage, signup, login, logout, home

urlpatterns = [
    path('', home, name=''),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', homepage, name='home'),
]
