from django.conf import settings
from django.utils import translation

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # جمع رموز اللغات مثل ['en','he','ar']
        self.lang_codes = [code for code, name in getattr(settings, "LANGUAGES", [])]

    def path_has_lang_prefix(self, path):
        # يفحص إذا كان المسار يبدأ ب /<lang>/ أو فقط /<lang>
        # مثال: /en/, /he/some/page
        for code in self.lang_codes:
            if path == f'/{code}' or path.startswith(f'/{code}/'):
                return True
        return False

    def __call__(self, request):
        # إذا طلب المستخدم مسار يضم بادئة لغة — لا نفعل شيئًا هنا
        if self.path_has_lang_prefix(request.path_info):
            # دع LocaleMiddleware أو منطق المسارات يتعامل مع اللغة
            return self.get_response(request)

        # إذا يوجد لغة محفوظة في الكوكي أو الجلسة فاحترمها
        lang_cookie = request.COOKIES.get('django_language')
        lang_session = request.session.get('django_language')

        if not lang_cookie and not lang_session:
            # لم يحدّد المستخدم لغة بعد: فعّل اللغة الافتراضية واحفظها في الجلسة
            translation.activate(settings.LANGUAGE_CODE)
            request.LANGUAGE_CODE = settings.LANGUAGE_CODE
            if hasattr(request, 'session'):
                request.session['django_language'] = settings.LANGUAGE_CODE
        else:
            # احترم اللغة المحفوظة
            active = lang_cookie or lang_session
            translation.activate(active)
            request.LANGUAGE_CODE = active

        response = self.get_response(request)
        translation.deactivate()
        return response
