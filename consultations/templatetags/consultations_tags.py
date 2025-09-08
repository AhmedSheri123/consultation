from django import template
from shortcuts.models import Shortcut  # استبدل باسم الموديل الحقيقي

register = template.Library()

# simple_tag لجلب كل العناصر
@register.simple_tag
def get_all_shortcuts():
    return Shortcut.objects.all()