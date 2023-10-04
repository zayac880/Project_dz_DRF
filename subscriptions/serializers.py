from rest_framework import serializers

from .models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Subscriber.
    """
    class Meta:
        model = Subscriber
        fields = '__all__'
