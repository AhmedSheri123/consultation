from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Shortcut, ICON_CHOICES 
from .forms import ShortcutForm
from dal import autocomplete
import requests

def shortcut_list(request):
    shortcuts = Shortcut.objects.all()
    return render(request, 'dashboard/shortcuts/list.html', {'shortcuts': shortcuts})


def shortcut_create(request):
    if request.method == 'POST':
        form = ShortcutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shortcut_list')  # صفحة قائمة الاختصارات
    else:
        form = ShortcutForm()
    return render(request, 'dashboard/shortcuts/shortcut_form.html', {'form': form, 'title': 'إضافة Shortcut'})

def shortcut_edit(request, pk):
    shortcut = get_object_or_404(Shortcut, pk=pk)
    if request.method == 'POST':
        form = ShortcutForm(request.POST, instance=shortcut)
        if form.is_valid():
            form.save()
            return redirect('shortcut_list')
    else:
        form = ShortcutForm(instance=shortcut)
    return render(request, 'dashboard/shortcuts/shortcut_form.html', {'form': form, 'title': 'تعديل Shortcut'})


def shortcut_create_ajax(request):
    data = dict()
    if request.method == 'POST':
        form = ShortcutForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            shortcuts = Shortcut.objects.all()
            data['html_table'] = render_to_string('dashboard/shortcuts/partial_table.html', {'shortcuts': shortcuts})
        else:
            data['form_is_valid'] = False
    else:
        form = ShortcutForm()
    context = {'form': form}
    data['html_form'] = render_to_string('dashboard/shortcuts/partial_form.html', context, request=request)
    return JsonResponse(data)

def shortcut_update_ajax(request, pk):
    shortcut = get_object_or_404(Shortcut, pk=pk)
    data = dict()
    if request.method == 'POST':
        form = ShortcutForm(request.POST, instance=shortcut)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            shortcuts = Shortcut.objects.all()
            data['html_table'] = render_to_string('dashboard/shortcuts/partial_table.html', {'shortcuts': shortcuts})
        else:
            data['form_is_valid'] = False
    else:
        form = ShortcutForm(instance=shortcut)
    context = {'form': form}
    data['html_form'] = render_to_string('dashboard/shortcuts/partial_form.html', context, request=request)
    return JsonResponse(data)

def shortcut_delete_ajax(request, pk):
    shortcut = get_object_or_404(Shortcut, pk=pk)
    data = dict()
    if request.method == 'POST':
        shortcut.delete()
        data['form_is_valid'] = True
        shortcuts = Shortcut.objects.all()
        data['html_table'] = render_to_string('dashboard/shortcuts/partial_table.html', {'shortcuts': shortcuts})
    else:
        context = {'shortcut': shortcut}
        data['html_form'] = render_to_string('dashboard/shortcuts/partial_delete.html', context, request=request)
    return JsonResponse(data)




class IconAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        q = self.q or ''
        # إرجاع tuples: (value, label) بدلاً من value فقط
        return [
            (icon_id, icon_name)
            for icon_id, icon_name in ICON_CHOICES
            if q.lower() in icon_name.lower() or q == ''
        ]

    def get_result_label(self, item):
        # DAL يتوقع أن item هو القيمة (icon_id)
        for icon_id, icon_name in ICON_CHOICES:
            if icon_id == item:
                return icon_name
        return item

    def get_selected_result_label(self, item):
        return self.get_result_label(item)
