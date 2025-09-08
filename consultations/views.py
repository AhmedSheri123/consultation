from django.shortcuts import render

# Create your views here.
import weasyprint

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Consultation
from clinic.models import ClinicInfo
from users.models import Patient
from .forms import ConsultationForm, ConsultationAttachmentForm

from django.http import JsonResponse
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .tables import ConsultationTable
from .filters import ConsultationFilter
from .forms import ConsultationForm
from django_tables2 import RequestConfig
from dal import autocomplete

# views.py
def consultation_list(request):
    queryset=Consultation.objects.all()
    if request.GET.get('patient'):
        queryset = queryset.filter(patient__id=request.GET.get('patient'))

    filter = ConsultationFilter(request.GET, queryset=queryset)
    table = ConsultationTable(filter.qs)
    RequestConfig(request).configure(table)
    context = {"table": table, "filter": filter}

    # استبدال is_ajax()
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html_table = render_to_string("dashboard/consultations/partial_consultation_table.html", context, request=request)
        html_filter = render_to_string("dashboard/consultations/partial_consultation_filter.html", context, request=request)
        return JsonResponse({"html_table": html_table, "html_filter": html_filter})

    return render(request, "dashboard/consultations/consultation_list.html", context)


def ConsultationCreate(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')  # أو أي صفحة تريد الذهاب إليها بعد الحفظ
    else:
        form = ConsultationForm()
        if request.GET.get('patient', None):
            form.initial = {
                'patient':Patient.objects.get(id=request.GET.get('patient'))
            }
        
    return render(request, 'dashboard/consultations/consultation_create.html', {'form': form})

def ConsultationEdit(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, request.FILES, instance=consultation)
        if form.is_valid():
            form.save()
            return redirect('consultation_list')  # أو أي صفحة تريد الذهاب إليها بعد الحفظ
    else:
        form = ConsultationForm(instance=consultation)
    return render(request, 'dashboard/consultations/consultation_create.html', {'form': form})


def save_consultation_form(request, form, template_name):
    data = {}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data["form_is_valid"] = True
            consultations = Consultation.objects.all()
            table = ConsultationTable(consultations)
            html_table = render_to_string(
                "dashboard/consultations/partial_consultation_table.html",
                {"table": table},
                request=request,
            )
            data["html_table"] = html_table
        else:
            data["form_is_valid"] = False
    context = {"form": form}
    data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def consultation_create_ajax(request):
    data = {}
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            filterset = ConsultationFilter(queryset=Consultation.objects.all())
            table = ConsultationTable(filterset.qs)
            RequestConfig(request).configure(table)
            data['form_is_valid'] = True
            data['html_table'] = render_to_string("dashboard/consultations/partial_consultation_table.html", {'table': table}, request=request)
        else:
            data['form_is_valid'] = False
    else:
        form = ConsultationForm()
    data['html_form'] = render_to_string("dashboard/consultations/partial_consultation_form.html", {'form': form}, request=request)
    return JsonResponse(data)


def consultation_edit_ajax(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == "POST":
        form = ConsultationForm(request.POST, instance=consultation)
    else:
        form = ConsultationForm(instance=consultation)
    return save_consultation_form(request, form, "dashboard/consultations/partial_consultation_edit.html")


def consultation_delete_ajax(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    data = {}
    if request.method == "POST":
        consultation.delete()
        data["form_is_valid"] = True
        consultations = Consultation.objects.all()
        table = ConsultationTable(consultations)
        data["html_table"] = render_to_string(
            "dashboard/consultations/partial_consultation_table.html",
            {"table": table},
            request=request,
        )
    else:
        context = {"consultation": consultation}
        data["html_form"] = render_to_string(
            "dashboard/consultations/partial_consultation_delete.html",
            context,
            request=request,
        )
    return JsonResponse(data)


# 🟢 تصدير PDF
def consultation_pdf(request, share_id):
    consultation = Consultation.objects.get(share_id=share_id)
    is_download = request.GET.get('download', None)
    clinic = ClinicInfo.objects.first()

    html = render_to_string("dashboard/consultations/print/temp1.html", {
        "consultation": consultation,
        "clinic":clinic
    })
    # html = consultation.medical_case
    pdf_file = weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()

    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="consultation_{consultation.id}.pdf"'
    if is_download:
        response["Content-Disposition"] = f'attachment; filename="consultation_{consultation.id}.pdf"'
    return response

def share_doc(request, share_id):
    consultation = Consultation.objects.get(share_id=share_id)
    return render(request, 'dashboard/consultations/share.html', {'consultation':consultation})


class PatientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Patient.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)  # عدل حسب الحقل عندك
        return qs