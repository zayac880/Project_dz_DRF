from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    last_name = models.CharField(max_length=150, verbose_name='имя')
    first_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', **NULLABLE)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.email}, {self.phone}, {self.city}, {self.avatar}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
