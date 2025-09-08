from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "email", "phone", "birth_date", "health_status", "national_id"]

