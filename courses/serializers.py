from rest_framework import serializers

from .models import Course, Lesson, Payment
from .validators import YoutubeValidate


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson.
    """
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidate(field='description'), YoutubeValidate(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course.
    """
    lessons = LessonSerializer(many=True, read_only=True, label='Уроки')
    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True, label='Количество уроков')

    class Meta:
        model = Course
        fields = '__all__'
        validators = [YoutubeValidate(field='description')]


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson.
    """
    class Meta:
        model = Payment
        fields = '__all__'
