from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_request, name='login'),
    path('loggedin', views.loggedin, name='loggedin'),
    path('logout', views.logout_view, name='logout'),
    path('loggedout', views.loggedout, name='loggedout'),
    path('created', views.createdaccount, name='created')
]