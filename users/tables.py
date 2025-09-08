import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from .models import Patient

class PatientTable(tables.Table):
    action = tables.Column(empty_values=(), verbose_name='الاجراءات')

    class Meta:
        model = Patient
        template_name = "django_tables2/bootstrap5.html"
        fields = ("name", "email", "phone", "birth_date", "health_status", "national_id")
        sequence = ("name", "email", "phone", "birth_date", "health_status", "national_id", "action")


    
    def render_action(self, record):
        url_add_consultation = reverse('ConsultationCreate')
        url_consultation_list = reverse('consultation_list')
        url_filemanager = reverse('FileManager', args=[record.id])
        url_edit = reverse('patient_edit_ajax', args=[record.id])
        url_delete = reverse('patient_delete_ajax', args=[record.id])
        return format_html(
            f"""
            <div class="dropdown  mb-2">
            <button class="btn btn-primary btn-sm dropdown-toggle" type="button" id="patientActions{ record.id }" data-bs-toggle="dropdown" aria-expanded="false">
                خيارات
            </button>
            <ul class="dropdown-menu" aria-labelledby="patientActions{ record.id }">
                <li>
                <a class="dropdown-item" href="{ url_add_consultation }?patient={ record.id }">
                    إضافة استشارة
                </a>
                </li>
                <li>
                <a class="dropdown-item" href="{ url_consultation_list }?patient={ record.id }">
                    عرض استشارات المريض
                </a>
                </li>
                <li>
                <a class="dropdown-item" href="{url_filemanager }">
                    مدير ملفات المريض
                </a>
                </li>


            </ul>

            </div>
                <button class="btn btn-sm btn-primary edit-patient-btn mb-2" data-url="{ url_edit }">
                    تعديل
                </button>
                <button class="btn btn-sm btn-danger delete-patient-btn mb-2" data-url="{ url_delete }">
                    حذف
                </button>

            """

        )