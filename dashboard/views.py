from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from users.models import Patient
from consultations.models import Consultation
from shortcuts.models import Shortcut
from website.models import ContactModel
from .filters import ContactFilter
from django_tables2 import RequestConfig
from .tables import ContactTable
@login_required
def dashboard(request):
    stats = {
        "patients_count": Patient.objects.count(),
        "consultations_count": Consultation.objects.count(),
        "shortcuts_count": Shortcut.objects.count(),
        "open_consultations": Consultation.objects.filter(status="open").count(),
    }

    latest_consultations = Consultation.objects.select_related("patient").order_by("-created_at")[:5]

    return render(request, "dashboard/home.html", {"stats": stats, "latest_consultations": latest_consultations})


def contact_list(request):
    queryset = ContactModel.objects.all().order_by('-creation_date')
    contact_filter = ContactFilter(request.GET, queryset=queryset)
    table = ContactTable(contact_filter.qs)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    
    return render(request, "dashboard/contact/contact-list.html", {
        "table": table,
        "filter": contact_filter
    })