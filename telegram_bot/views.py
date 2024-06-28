from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TelegramUser
from .serializers import TelegramUserSerializer

class TelegramUserViewSet(viewsets.ModelViewSet):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
