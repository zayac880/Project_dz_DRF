from rest_framework import serializers

from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели Course.
        Поля:
        - id: Идентификатор курса (автогенерируется)
        - title: Название курса
        - preview: Превью курса (картинка)
        - description: Описание курса
        """
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """
       Сериализатор для модели Lesson.
       Поля:
       - id: Идентификатор урока (автогенерируется)
       - title: Название урока
       - description: Описание урока
       - preview: Превью урока (картинка)
       - video_link: Ссылка на видео урока
       """
    class Meta:
        model = Lesson
        fields = '__all__'
