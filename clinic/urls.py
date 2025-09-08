from django.urls import path
from . import views

urlpatterns = [
    path('clinic_info', views.clinic_info, name='clinic_info')
]
