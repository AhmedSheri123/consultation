from django.db import models
from froala_editor.fields import FroalaField
from .libs import ICON_CHOICES


class Shortcut(models.Model):
    title = models.CharField(max_length=50, null=True)  # مثال: "ضغط الدم مرتفع"
    code = FroalaField()  # مثال: :bp
    ico = models.CharField(max_length=50, choices=ICON_CHOICES)  # حقل اختيار
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
