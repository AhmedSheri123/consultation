"""
URL configuration for consultation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from website.views import PrivacyPolicy

urlpatterns = [
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('PrivacyPolicy', PrivacyPolicy, name='PrivacyPolicy'),
    path("froala_editor/", include("froala_editor.urls")),

] + i18n_patterns(
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),

    path('dashboard/patients/', include('users.urls')),
    path('dashboard/shortcuts/', include('shortcuts.urls')),
    path('dashboard/clinic/', include('clinic.urls')),
    path('dashboard/consultations/', include('consultations.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('filemanager/', include('filemanager.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)