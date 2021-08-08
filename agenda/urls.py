from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', RedirectView.as_view(url='/agenda/')),

]