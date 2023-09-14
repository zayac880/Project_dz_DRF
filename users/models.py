from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='почта'
    )

    phone = models.CharField(
        max_length=35,
        verbose_name='телефон',
        **NULLABLE
    )
    city = models.CharField(
        max_length=100,
        verbose_name='город',
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='аватар',
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}, {self.phone}, {self.city}, {self.avatar}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
