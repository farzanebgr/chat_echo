from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chat/', include('echo_app.urls')),
    path('admin/', admin.site.urls),
]
