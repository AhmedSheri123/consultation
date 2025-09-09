from django.db import models
from froala_editor.fields import FroalaField
import uuid
from .libs import remove_watermark
# Create your models here.

def generate_uuid16():
    return uuid.uuid4().hex[:16]

class Consultation(models.Model):
    STATUS_CHOICES = [
        ("new", "جديدة"),
        ("review", "قيد المراجعة"),
        ("done", "منتهية"),
    ]

    patient = models.ForeignKey("users.Patient", on_delete=models.CASCADE, related_name="consultations")
    title = models.CharField(max_length=254, default="new")
    medical_case = FroalaField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    share_id = models.CharField(
        max_length=16,
        unique=True,
        editable=False,
        default=generate_uuid16
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"استشارة {self.patient.name} - {self.created_at.date()}"

    class Meta:
        ordering = ["-created_at"]  # 👈 الترتيب الافتراضي

    def save(self, *args, **kwargs):
        # تنظيف المحتوى باستخدام BeautifulSoup
        if self.content:
            self.content = str(remove_watermark(self.content))

        super().save(*args, **kwargs)


class ConsultationAttachment(models.Model):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="consultation_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)