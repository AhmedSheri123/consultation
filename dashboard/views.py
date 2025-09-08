from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from users.models import Patient
from consultations.models import Consultation
from shortcuts.models import Shortcut


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
