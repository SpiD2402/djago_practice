from rest_framework.routers import DefaultRouter
from .views import LanguageViewSet

router = DefaultRouter()
router.register('', LanguageViewSet,basename = 'languages')

urlpatterns = router.urls