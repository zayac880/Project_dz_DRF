from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Создать пользовательского суперпользователя'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = "admin@admin.ru"
        password = "admin123wqe123"
        user, created = User.objects.get_or_create(email=email)
        if created:
            user.is_superuser = True
            user.is_staff = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан'))
        else:
            self.stdout.write(self.style.SUCCESS('Суперпользователь уже существует'))
