from django.urls import path
from .views import Homepage, signup, login, logout, Home, viewCRUD, viewCRUD2

urlpatterns = [
    path('', Home.as_view(), name=''),
    path('crud/', viewCRUD.as_view(), name='crud'),
    path('crud2/<int:id>/', viewCRUD2.as_view(), name='crud2'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', Homepage.as_view(), name='homepage'),
]
