from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from django.http import JsonResponse
from django.template.loader import render_to_string

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .models import Patient
from .tables import PatientTable
from .filters import PatientFilter
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django_tables2 import RequestConfig

class PatientListView(SingleTableMixin, FilterView):
    model = Patient
    table_class = PatientTable
    template_name = "dashboard/users/patient_list.html"
    filterset_class = PatientFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PatientForm()  # الفورم موجود في context
        return context



def add_patient_ajax(request):
    data = dict()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            patients = Patient.objects.all()
            table = PatientTable(patients)
            table.paginate(page=1, per_page=10)
            data['html_table'] = render_to_string('dashboard/users/partial_patient_table.html', {'table': table}, request=request)
        else:
            data['form_is_valid'] = False
    else:
        form = PatientForm()
    
    context = {'form': form}
    data['html_form'] = render_to_string('dashboard/users/partial_patient_add.html', context, request=request)
    return JsonResponse(data)

def edit_patient_ajax(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    data = dict()

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            patients = Patient.objects.all()
            table = PatientTable(patients)
            RequestConfig(request, paginate={'per_page': 10}).configure(table)
            data['html_table'] = render_to_string(
                'dashboard/users/partial_patient_table.html',
                {'table': table},
                request=request
            )
        else:
            data['form_is_valid'] = False
    else:
        form = PatientForm(instance=patient)

    context = {'form': form}
    data['html_form'] = render_to_string(
        'dashboard/users/partial_patient_edit.html',
        context,
        request=request
    )
    return JsonResponse(data)


def delete_patient_ajax(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    data = dict()

    if request.method == 'POST':
        patient.delete()
        data['form_is_valid'] = True
        patients = Patient.objects.all()
        table = PatientTable(patients)
        RequestConfig(request, paginate={'per_page': 10}).configure(table)
        data['html_table'] = render_to_string(
            'dashboard/users/partial_patient_table.html',
            {'table': table},
            request=request
        )
    else:
        context = {'patient': patient}
        data['html_form'] = render_to_string(
            'dashboard/users/partial_patient_delete.html',
            context,
            request=request
        )

    return JsonResponse(data)


class PatientDetailView(DetailView):
    model = Patient
    template_name = "dashboard/users/patient_detail.html"
    context_object_name = "patient"

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "dashboard/users/patient_edit.html"

    # بعد الحفظ يرجع لصفحة تفاصيل المريض
    def get_success_url(self):
        return reverse_lazy("patient_detail", kwargs={"pk": self.object.pk})
    

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "dashboard/users/patient_delete.html"
    success_url = reverse_lazy("patients_list")