from django.urls import path
from . import views

urlpatterns = [
    path("", views.consultation_list, name="consultation_list"),
    path("create/", views.ConsultationCreate, name="ConsultationCreate"),
    path("add/", views.consultation_create_ajax, name="consultation_create_ajax"),
    path("<int:pk>/edit/", views.ConsultationEdit, name="ConsultationEdit"),
    path("<int:pk>/delete/", views.consultation_delete_ajax, name="consultation_delete_ajax"),

    path("<str:share_id>/pdf/", views.consultation_pdf, name="consultation_pdf"),
    path("<str:share_id>/share_doc/", views.share_doc, name="share_doc"),
    path('patient-autocomplete/', views.PatientAutocomplete.as_view(), name='patient-autocomplete'),

]