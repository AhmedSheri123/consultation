import json
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(settings.BASE_DIR)
icons_file = BASE_DIR / 'shortcuts' / 'bootstrap-icons.json'

# تحميل البيانات
with open(icons_file, 'r', encoding='utf-8') as f:
    icons_data = json.load(f)

# إنشاء قائمة ICON_CHOICES
ICON_CHOICES = [
    (f"bi-{icon}", f"{icon.replace('-', ' ').title()}")  # استخدم icon مباشرة لأنه string
    for icon in icons_data
]

