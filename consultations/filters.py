import django_filters
from django import forms
from .models import Consultation
from users.models import Patient
from dal import autocomplete

class ConsultationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_by_name', label="الاسم",
                                        
                                        widget=forms.TextInput(attrs={'placeholder': 'بحث بالاسم', "class":'col-2'})
                                        )
    start_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='gte', label='من تاريخ',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='lte', label='إلى تاريخ',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    search_id = django_filters.CharFilter(
        method='filter_by_national_id', label='رقم الهوية',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهوية'})
    )

    class Meta:
        model = Consultation
        fields = ['name', "search_id", "status", "start_date", "end_date"]

    def filter_by_national_id(self, queryset, name, value):
        return queryset.filter(patient__national_id__icontains=value)

    def filter_by_name(self, queryset, name, value):
        return queryset.filter(patient__name__icontains=value)
