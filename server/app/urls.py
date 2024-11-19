from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/<str:id>', views.Login),
]
