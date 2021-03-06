# Django
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

# local Django
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ndtv/', include('ndtv.urls')),
    url(r'^$', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
