from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny

from .paginators import CoursesPaginator
from .permissions import IsManagers
from django_filters.rest_framework import DjangoFilterBackend

from .models import Course, Lesson, Payment
from .serializers import CourseSerializer, LessonSerializer, PaymentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsManagers]
    permission_classes = [AllowAny]
    serializer_class = CourseSerializer
    pagination_class = CoursesPaginator

    def get_queryset(self):
        queryset = Course.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class LessonCreateAPIView(generics.CreateAPIView):
    """
    Создать новый урок.
    """
    permission_classes = [IsManagers]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(generics.ListAPIView):
    """
    Получить список всех уроков.
    """
    serializer_class = LessonSerializer
    pagination_class = CoursesPaginator

    def get_queryset(self):
        queryset = Lesson.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    Получить конкретный урок.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    Обновить существующий урок.
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    Удалить существующий урок.
    """
    permission_classes = [IsManagers]
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    """
    Получить список всех платежей.
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('pay_course', 'payment_method')
    ordering_fields = ('pay_date',)
    pagination_class = CoursesPaginator