from django import forms
from .models import Consultation, ConsultationAttachment
from froala_editor.widgets import FroalaEditor
from dal import autocomplete

class ConsultationForm(forms.ModelForm):
    # medical_case = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Consultation
        fields = ['patient', 'status', 'title', 'medical_case']

        widgets = {
            'patient': autocomplete.ModelSelect2(
                url='patient-autocomplete',
                attrs={
                    'class': 'p-2'
                }
            ),
            'medical_case': FroalaEditor(),
        }


class ConsultationAttachmentForm(forms.ModelForm):
    class Meta:
        model = ConsultationAttachment
        fields = ["file"]
