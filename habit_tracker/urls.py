from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # маршруты для регистрации и авторизации
    path('api/', include('habits.urls')),  # маршруты для работы с привычками
    path('api/telegram/', include('telegram_bot.urls')),  # маршруты для Telegram
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
