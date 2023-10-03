# Generated by Django 4.2.5 on 2023-09-14 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_preview_alter_lesson_preview_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course', verbose_name='курс'),
        ),
    ]