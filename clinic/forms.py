from django import forms
from .models import ClinicInfo

class ClinicForm(forms.ModelForm):
    class Meta:
        model = ClinicInfo
        fields = ['name', 'clinic_info', 'logo', 'phone', 'email', 'address', 'website']
