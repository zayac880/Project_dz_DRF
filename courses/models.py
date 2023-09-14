from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    """
    Модель для представления курсов.
    - id: Идентификатор курса (автогенерируется)
    - title: Название курса
    - preview: Превью курса (картинка)
    - description: Описание курса
    """
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )
    preview = models.ImageField(
        upload_to='course_previews/',
        verbose_name='превью',
        **NULLABLE
    )
    description = models.TextField(
        verbose_name='описание'
    )

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
    title = models.CharField(
        max_length=100,
        verbose_name='название'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    preview = models.ImageField(
        upload_to='lesson_previews/',
        verbose_name='превью',
        **NULLABLE
    )
    video_link = models.URLField(
        verbose_name='ссылка на видео',
        **NULLABLE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='курс',
        **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.preview}, {self.video_link}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Payment(models.Model):
    """
    Модель для представления уроков.
    - id: Идентификатор платежа (автогенерируется)
    - user: пользователь для оплаты
    - pay_date: Название платежа
    - description: Описание платежа
    - preview: Превью урока (картинка)
    - video_link: Ссылка на видеоурок
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    pay_date = models.DateField(
        verbose_name='дата оплаты'
    )
    pay_course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        verbose_name='оплаченный курс'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='сумма оплаты'
    )
    payment_method = models.CharField(
        max_length=150,
        choices=[('cash', 'наличные'), ('transfer', 'перевод на счет')],
        verbose_name='способ оплаты'
    )

    def __str__(self):
        return f'Платеж от {self.user.username} за {self.pay_course}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
