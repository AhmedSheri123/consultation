from django import forms
from dal import autocomplete
from .models import Shortcut

class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ['title', 'ico', 'code']
        widgets = {
            'ico': autocomplete.ListSelect2(url='icon-autocomplete'),  # يربط DAL بالـ view
        }
