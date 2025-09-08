from django.urls import path
from . import views

urlpatterns = [
    path("", views.PatientListView.as_view(), name="patients_list"),  # /users/
    path('patients/add/', views.add_patient_ajax, name='patient_add_ajax'),
    path('<int:pk>/edit/', views.edit_patient_ajax, name='patient_edit_ajax'),
    path('patients/<int:pk>/delete/', views.delete_patient_ajax, name='patient_delete_ajax'),


    path("<int:pk>/", views.PatientDetailView.as_view(), name="patient_detail"),   # /users/5/
    path("<int:pk>/edit/", views.PatientUpdateView.as_view(), name="patient_edit"),
    path("<int:pk>/delete/", views.PatientDeleteView.as_view(), name="patient_delete"),
]
