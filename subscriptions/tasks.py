from celery import shared_task
from django.core.mail import send_mail


@shared_task
def mail(course_id, email):
    print('Идёт отправка')
    response = send_mail(
        subject='Обновление курса',
        message=f'Курс {course_id} обновлен!',
        from_email=None,
        recipient_list=[email],
    )
