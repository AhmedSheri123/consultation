# filters.py
import django_filters
from website.models import ContactModel

class ContactFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains', label="Full Name")
    email = django_filters.CharFilter(lookup_expr='icontains', label="Email")
    

    class Meta:
        model = ContactModel
        fields = ['full_name', 'email']
