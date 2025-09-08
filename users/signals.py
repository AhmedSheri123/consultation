import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient
from django.conf import settings

@receiver(post_save, sender=Patient)
def consultation_created(sender, instance, created, **kwargs):
    if created:
        user_dir = os.path.join(settings.MEDIA_ROOT, "manager", str(instance.id))
        
        # لو المجلد مش موجود، ينشأ
        os.makedirs(user_dir, exist_ok=True)