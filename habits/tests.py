# habits/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from .models import Habit

class HabitTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser@example.com', password='testpass')
        self.client.login(email='testuser@example.com', password='testpass')

    def test_create_habit(self):
        url = reverse('habit-list-create')
        data = {
            'action': 'Test Action',
            'time': '12:00:00',
            'place': 'Test Place',
            'is_pleasant': False,
            'period': 1,
            'reward': 'Test Reward',
            'duration': 60,
            'is_public': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_habits(self):
        url = reverse('habit-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
