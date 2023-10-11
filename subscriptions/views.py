from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberAPIView(APIView):
    """
    Создать подписчика.
    """

    def post(self, request, course_id):
        user = request.user
        serializer = SubscriberSerializer(data={'user': user.pk, 'course': course_id})
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': f'Вы успешно подписались на курс №{course_id}'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_404_NOT_FOUND)


class SubscriberPIView(APIView):
    """
    Удалить подписчика.
    """
    def delete(self, request, course_id):
        user = request.user
        try:
            subscriber = Subscriber.objects.get(user=user, course=course_id)
        except Subscriber.DoesNotExist:
            return Response(
                {'detail': 'Подписчик не найден.'},
                status=status.HTTP_404_NOT_FOUND
            )
        subscriber.delete()
        return Response(
            {'message': f'Вы успешно удалили подписчика и отписались от курса №{course_id}'},
            status=status.HTTP_204_NO_CONTENT
        )
