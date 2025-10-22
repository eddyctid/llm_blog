from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()
router.register(r'posts', PostModelViewSet, basename='posts')

urlpatterns = router.urls