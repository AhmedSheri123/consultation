from django.db import models

# Create your models here.
class ClinicInfo(models.Model):
    name = models.CharField(max_length=255)
    clinic_info = models.TextField(null=True)
    logo = models.ImageField(upload_to="clinic/", null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    website = models.URLField("الموقع الإلكتروني", blank=True, null=True)
    
    def __str__(self):
        return self.name
