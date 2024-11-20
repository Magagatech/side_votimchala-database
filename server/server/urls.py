from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from app.views import RolesViewSet, StudentViewSet, ElectionViewSet, PositionViewSet, CandidateViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'roles', RolesViewSet)
router.register(r'students', StudentViewSet)
router.register(r'elections', ElectionViewSet)
router.register(r'positions', PositionViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'votes', VoteViewSet)
# router.register(r'election', ElectionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('apk/', include('app.urls')),

]
