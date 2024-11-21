from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('election/', views.ElectionView.as_view(), name='election'),
]
