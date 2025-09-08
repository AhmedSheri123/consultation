from django.urls import path
from . import views

urlpatterns = [
    path('', views.shortcut_list, name='shortcut_list'),
    path('shortcuts/create/', views.shortcut_create, name='shortcut_create'),
    path('shortcuts/<int:pk>/edit/', views.shortcut_edit, name='shortcut_edit'),
    path('create/', views.shortcut_create_ajax, name='shortcut_create_ajax'),
    path('update/<int:pk>/', views.shortcut_update_ajax, name='shortcut_update_ajax'),
    path('delete/<int:pk>/', views.shortcut_delete_ajax, name='shortcut_delete_ajax'),
    path('icon-autocomplete/', views.IconAutocomplete.as_view(), name='icon-autocomplete'),

]
