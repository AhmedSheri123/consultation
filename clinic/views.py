from django.shortcuts import render, redirect
from .forms import ClinicForm
from .models import ClinicInfo



def clinic_info(request):
    clinic = ClinicInfo.objects.first()
    if not clinic: 
        clinic = ClinicInfo.objects.create().save()
    

    if request.method == "POST":
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('clinic_info')
    else:
        form = ClinicForm(instance=clinic)
    return render(request, "dashboard/clinic/clinic_info.html", {"form": form})