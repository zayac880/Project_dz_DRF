from django.urls import path
from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, PaymentAPIView

# Получаем имя приложения
app_name = CoursesConfig.name

# Создаем DefaultRouter для CourseViewSet
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-pk'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path('make-payment/<int:course_id>/', PaymentAPIView.as_view(), name='make-payment'),
] + router.urls
