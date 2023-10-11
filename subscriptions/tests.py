from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from subscriptions.models import Subscriber
from users.models import User
from courses.models import Course


class CoursesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser@email',
            password='testpassword'
        )
        self.course = Course.objects.create(
            title='Название курса',
            description='Описание курса'
        )

        Subscriber.objects.filter(
            user=self.user,
            course=self.course
        ).delete()

    def test_create_subscriber(self):
        self.client.force_authenticate(user=self.user)
        create_subscriber = reverse(
            'subscriptions:subscribe',
            kwargs={'course_id': self.course.id}
        )

        response = self.client.post(create_subscriber)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Subscriber.objects.filter(
                user=self.user,
                course=self.course
            ).exists()
        )

    def test_delete_subscriber(self):
        self.client.force_authenticate(user=self.user)
        delete_subscriber = reverse(
            'subscriptions:unsubscribe',
            kwargs={'course_id': self.course.id}
        )

        if Subscriber.objects.filter(user=self.user, course=self.course).exists():
            response = self.client.delete(delete_subscriber)
            print(response.json())

            self.assertEqual(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )

            self.assertFalse(
                Subscriber.objects.filter(user=self.user, course=self.course).exists()
            )
        else:
            print("Подписчик не существует")
