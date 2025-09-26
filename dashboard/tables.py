# tables.py
import django_tables2 as tables
from website.models import ContactModel

class ContactTable(tables.Table):
    full_name = tables.Column(verbose_name="Full Name")
    email = tables.Column(verbose_name="Email")
    phone_number = tables.Column(verbose_name="Phone Number")
    project_description = tables.Column(verbose_name="Project Description")
    creation_date = tables.DateTimeColumn(format="Y-m-d H:i", verbose_name="Creation Date")

    class Meta:
        model = ContactModel
        template_name = "django_tables2/bootstrap5.html"  # أو bootstrap4 حسب المشروع
        fields = ("full_name", "email", "phone_number", "project_description", "creation_date")
