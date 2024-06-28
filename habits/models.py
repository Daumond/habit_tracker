from django.db import models
from django.conf import settings


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                      related_name='related_to')
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True, null=True)
    duration = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.action} at {self.time} in {self.place}'
