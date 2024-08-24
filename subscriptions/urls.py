from django.urls import path

from .apps import SubscriptionsConfig
from .views import CourseSubscriptionToggleAPIView


app_name = SubscriptionsConfig.name
urlpatterns = [
    path("", CourseSubscriptionToggleAPIView.as_view(), name="course-subscribe"),
]
