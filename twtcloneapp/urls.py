from django.urls import path
from .views import homepage, signup, login, logout

urlpatterns = [
    path('', homepage, name=''),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', homepage, name='home'),
]
