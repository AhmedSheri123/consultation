from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('contacts/', views.contact_list, name='contact-list'),
]
