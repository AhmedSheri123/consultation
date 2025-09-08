import django_filters
from .models import Patient
from django import forms

class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="الاسم",
                                     
                                     widget=forms.TextInput(attrs={'placeholder': 'بحث بالاسم', "class":'col-2'})
                                     )
    phone = django_filters.CharFilter(lookup_expr="icontains", label="الهاتف")
    national_id = django_filters.CharFilter(lookup_expr="icontains", label="رقم الهوية")

    class Meta:
        model = Patient
        fields = ["name", "phone", "national_id"]
