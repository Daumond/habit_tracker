from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Habit
from .serializers import HabitSerializer
from .permissions import IsOwnerOrReadOnly


class HabitPagination(PageNumberPagination):
    page_size = 5


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.action == 'list':
            return Habit.objects.filter(is_public=True) | Habit.objects.filter(user=self.request.user)
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
