from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Web App
    path('', include('core.urls')),
    # API
    path('api/', include('core.api_urls')),
]