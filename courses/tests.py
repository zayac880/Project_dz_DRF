from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='testuser@email', password='testpassword')
        self.course = Course.objects.create(title='Название курса', description='Описание курса')

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
