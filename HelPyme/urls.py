from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logistica/', include('logistica.urls')),
]
