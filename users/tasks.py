from celery import shared_task
from datetime import datetime, timedelta

from users.models import User


@shared_task
def deactivate_user():
    date_deactivate = datetime.now() - timedelta(days=30)
    users_queryset = User.objects.filter(last_login__lt=date_deactivate)
    users_queryset.update(is_active=False)

