from rest_framework.routers import DefaultRouter
from .views import UserViewSet,GroupViewSet

router = DefaultRouter()

router.register('users',UserViewSet,basename='users')
router.register('groups',GroupViewSet,basename='groups')


urlpatterns = router.urls








