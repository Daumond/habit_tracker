from rest_framework.routers import DefaultRouter
from .views import TelegramUserViewSet

router = DefaultRouter()
router.register(r'telegram_users', TelegramUserViewSet, basename='telegram_user')

urlpatterns = router.urls
