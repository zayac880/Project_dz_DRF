from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from courses.models import Course, Lesson
from users.models import User


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@email', password='testpassword')
        self.course = Course.objects.create(title='Название курса', description='Описание курса')
        self.lesson = Lesson.objects.create(
            title='Название урока',
            description='Описание урока',
            preview=None,
            video_link='https://youtube.com',
            owner=self.user,
            course=self.course,
        )

    def test_create_course(self):
        """Тест создания курса"""
        data = {
            'title': 'test',
            'description': 'test description',
        }
        response = self.client.post(
            '/courses/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        self.assertEqual(
            response.json()['title'],
            'test',
        )
        self.assertTrue(
            Course.objects.filter(title='test').exists(),
        )

    def test_list_course(self):
        """Тест вывода списка курсов"""
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/courses/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)

        data = {
            "title": "test_new",
            "course": self.course.id,
            "video_link": "https://youtube.com",
            "user_id": self.user.id,
        }

        update_lesson = reverse(
            'courses:lesson-update',
            kwargs={'pk': self.lesson.pk}
        )
        response = self.client.patch(
            update_lesson,
            data,
            format='json',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)

        delete_lesson = reverse(
            'courses:lesson-delete',
            kwargs={'pk': self.lesson.pk}
        )

        response = self.client.delete(delete_lesson)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.filter(
                pk=self.lesson.pk
            ).exists()
        )
