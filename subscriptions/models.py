from django.db import models

from courses.models import Course
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Subscriber(models.Model):

    user = models.ForeignKey(
        User,
        related_name="subscriber",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course,
        related_name="subscriber",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    subscribed = models.BooleanField(default=False)

    class Meta:
        unique_together = [['user', 'course']]
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

