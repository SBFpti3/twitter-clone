from django.urls import path
from .views import Homepage, signup, user_login, user_logout, Home, viewCRUD, viewCRUD2, error_view
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('crud/', viewCRUD.as_view(), name='crud'),
    path('edit/<int:id>', viewCRUD2.as_view(), name='edit'),
    path('signup', signup, name='signup'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('home', Homepage.as_view(), name='homepage'),
    path('error', error_view, name='error'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]