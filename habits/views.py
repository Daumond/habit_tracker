from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Habit
from .serializers import HabitSerializer


class HabitPagination(PageNumberPagination):
    page_size = 5


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        if self.action == 'list':
            return Habit.objects.filter(is_public=True) if self.request.user.is_anonymous else Habit.objects.filter(user=self.request.user)
        return Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
