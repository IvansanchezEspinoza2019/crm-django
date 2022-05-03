
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page),
    path('leads/', include("leads.urls", namespace="leads")),
    path("login", LoginView.as_view(), name="login")
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )