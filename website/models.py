from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class ContactModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=("Email address"))
    phone_number = models.CharField(max_length=100, verbose_name=("Phone Number"))
    project_description = models.TextField(verbose_name=("Project Description"))

    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.full_name)