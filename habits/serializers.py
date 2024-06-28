from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        if data['duration'] > 120:
            raise serializers.ValidationError("Duration must be less than or equal to 120 seconds.")
        if data['related_habit'] and data['reward']:
            raise serializers.ValidationError("Both related_habit and reward cannot be set at the same time.")
        if data['related_habit'] and not data['related_habit'].is_pleasant:
            raise serializers.ValidationError("Related habit must be a pleasant habit.")
        if data['is_pleasant'] and (data.get('related_habit') or data.get('reward')):
            raise serializers.ValidationError("Pleasant habit cannot have related_habit or reward.")
        if data['frequency'] > 7:
            raise serializers.ValidationError("Habit frequency cannot be more than 7 days.")
        return data
