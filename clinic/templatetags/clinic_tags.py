from django import template
from clinic.models import ClinicInfo  # استبدل باسم الموديل الحقيقي

register = template.Library()

# simple_tag لجلب كل العناصر
@register.simple_tag
def get_clinic_info():
    return ClinicInfo.objects.first()