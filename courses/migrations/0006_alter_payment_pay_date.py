# Generated by Django 4.2.5 on 2023-10-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_date',
            field=models.DateField(auto_now_add=True, verbose_name='дата оплаты'),
        ),
    ]
