
from django.contrib import admin
from django.urls import path
from core.views import hello_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello_api, name='hello_api'),
]

