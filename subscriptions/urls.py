from django.urls import path

from subscriptions.apps import SubscribtionsConfig
from subscriptions.views import SubscriberAPIView, SubscriberPIView

app_name = SubscribtionsConfig.name


urlpatterns = [
    path('subscribe/<int:course_id>/', SubscriberAPIView.as_view(), name='subscribe'),
    path('unsubscribe/<int:course_id>/', SubscriberPIView.as_view(), name='unsubscribe'),
]