from django.urls import path
from . import views

urlpatterns = [
    path('Signup', views.Signup, name='Signup'),
    path('Login', views.Login, name='Login'),
    path('Logout', views.Logout, name='Logout'),
]
