# tables.py
import django_tables2 as tables
from .models import Consultation

class ConsultationTable(tables.Table):
    actions = tables.TemplateColumn(template_name="dashboard/consultations/consultation_actions.html", orderable=False)

    class Meta:
        model = Consultation
        template_name = "django_tables2/bootstrap5.html"
        fields = ("patient", "title", "status", "created_at")
