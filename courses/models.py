from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """
    Модель для представления курсов.
    - id: Идентификатор курса (автогенерируется)
    - title: Название курса
    - preview: Превью курса (картинка)
    - description: Описание курса
    """
    title = models.CharField(max_length=100, verbose_name='название')
    preview = models.ImageField(upload_to='course_previews/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}, {self.preview}, {self.description}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """
     Модель для представления уроков.
     - id: Идентификатор урока (автогенерируется)
     - title: Название урока
     - description: Описание урока
     - preview: Превью урока (картинка)
     - video_link: Ссылка на видеоурок
     """
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson_previews/', verbose_name='превью', **NULLABLE)
    video_link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.preview}, {self.video_link}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
