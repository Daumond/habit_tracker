from celery import shared_task
from .models import TelegramUser
from .bot import send_telegram_message

@shared_task
def send_reminders():
    for telegram_user in TelegramUser.objects.filter(is_active=True):
        habits = Habit.objects.filter(user=telegram_user.user, is_public=True)
        for habit in habits:
            message = f"Reminder: {habit.action} at {habit.time} in {habit.place}"
            send_telegram_message(telegram_user.telegram_id, message)
