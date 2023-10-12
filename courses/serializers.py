from rest_framework import serializers

from .models import Course, Lesson, Payment
from .validators import YoutubeValidate, check_payment_method, check_card_number, check_expiry_month, check_expiry_year, \
    check_cvc


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
    Сериализатор для модели Payment.
    """
    class Meta:
        model = Payment
        fields = '__all__'


class CardInformationSerializer(serializers.Serializer):
    payment_method = serializers.CharField(
        max_length=50,
        required=True,
        validators=[check_payment_method]
    )
    card_number = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_card_number]
    )
    expiry_month = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_month],
    )
    expiry_year = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_expiry_year],
    )
    cvc = serializers.CharField(
        max_length=150,
        required=True,
        validators=[check_cvc],
    )
