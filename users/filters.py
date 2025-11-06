import django_filters
from .models import Patient
from django import forms

class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="name",
                                     
                                     widget=forms.TextInput(attrs={'placeholder': 'search by name', "class":'col-2'})
                                     )
    phone = django_filters.CharFilter(lookup_expr="icontains", label="phone")
    national_id = django_filters.CharFilter(lookup_expr="icontains", label="national id")

    class Meta:
        model = Patient
        fields = ["name", "phone", "national_id"]
