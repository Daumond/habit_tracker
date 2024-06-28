from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from habits.models import Habit
from datetime import time

User = get_user_model()


class HabitTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='password123')
        self.habit = Habit.objects.create(user=self.user, place='Gym', time=time(18, 0), action='Workout', is_pleasant=False, frequency=1, reward='Protein shake', duration=30, is_public=True)

    def test_habit_creation(self):
        self.assertEqual(self.habit.user, self.user)
        self.assertEqual(self.habit.place, 'Gym')
        self.assertEqual(self.habit.time, time(18, 0))
        self.assertEqual(self.habit.action, 'Workout')
        self.assertFalse(self.habit.is_pleasant)
        self.assertEqual(self.habit.frequency, 1)
        self.assertEqual(self.habit.reward, 'Protein shake')
        self.assertEqual(self.habit.duration, 30)
        self.assertTrue(self.habit.is_public)

    def test_habit_str(self):
        self.assertEqual(str(self.habit), 'Workout at Gym')

    def test_habit_duration_validation(self):
        with self.assertRaises(ValueError):
            self.habit.duration = 150
            self.habit.save()

class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', password='password123')
        self.client.login(email='testuser@example.com', password='password123')
        self.habit = Habit.objects.create(user=self.user, place='Gym', time=time(18, 0), action='Workout', is_pleasant=False, frequency=1, reward='Protein shake', duration=30, is_public=True)

    def test_habit_list(self):
        url = reverse('habit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_habit_detail(self):
        url = reverse('habit-detail', args=[self.habit.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], 'Workout')

    def test_habit_create(self):
        url = reverse('habit-list')
        data = {
            'place': 'Park',
            'time': '07:00:00',
            'action': 'Jogging',
            'is_pleasant': False,
            'frequency': 1,
            'duration': 20,
            'reward': 'Smoothie',
            'is_public': True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        url = reverse('habit-detail', args=[self.habit.id])
        data = {
            'place': 'Home Gym',
            'time': '19:00:00',
            'action': 'Yoga',
            'is_pleasant': False,
            'frequency': 1,
            'duration': 30,
            'reward': 'Tea',
            'is_public': True
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, 'Home Gym')
        self.assertEqual(self.habit.action, 'Yoga')

    def test_habit_delete(self):
        url = reverse('habit-detail', args=[self.habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
