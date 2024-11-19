from rest_framework.routers import DefaultRouter

from django.contrib import admin
from django.urls import path, include
from app.views import UserViewSet

# framework stuff
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
