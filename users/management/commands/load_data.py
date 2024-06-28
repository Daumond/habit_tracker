from django.contrib.auth import get_user_model

from .habits.models import Habit
from datetime import time

User = get_user_model()

# Создание пользователя
user1 = User.objects.create_user(
    email='user1@example.com',
    password='password123',
    phone='1234567890',
    country='Country1',
    first_name='First1',
    last_name='Last1')
user2 = User.objects.create_user(
    email='user2@example.com',
    password='password123',
    phone='0987654321',
    country='Country2',
    first_name='First2',
    last_name='Last2')

# Создание привычек для пользователя 1
habit1 = Habit.objects.create(
    user=user1, place='Gym',
    time=time(18, 0),
    action='Workout', is_pleasant=False,
    frequency=1,
    reward='Protein shake',
    duration=30,
    is_public=True)
habit2 = Habit.objects.create(
    user=user1,
    place='Park',
    time=time(7, 0),
    action='Jogging',
    is_pleasant=False,
    frequency=1,
    related_habit=habit1,
    duration=20,
    is_public=True)

# Создание приятной привычки для пользователя 1
pleasant_habit = Habit.objects.create(
    user=user1, place='Home',
    time=time(19, 0),
    action='Watch TV',
    is_pleasant=True,
    frequency=1,
    duration=30,
    is_public=False)

# Создание привычек для пользователя 2
habit3 = Habit.objects.create(
    user=user2,
    place='Office',
    time=time(9, 0),
    action='Check emails',
    is_pleasant=False,
    frequency=5,
    reward='Coffee',
    duration=10,
    is_public=True)
