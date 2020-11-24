from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import include, path


urlpatterns = [
    path('logistica/', include('logistica.urls')),

]

