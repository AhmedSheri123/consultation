from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    health_status = models.TextField(blank=True, null=True)
    national_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PatientActivity(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="activities")
    action = models.CharField(max_length=255)  # مثال: "تمت إضافة استشارة"
    created_at = models.DateTimeField(auto_now_add=True)
