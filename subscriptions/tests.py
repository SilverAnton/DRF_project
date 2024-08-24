from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from courses.models import Course
from subscriptions.models import CourseSubscription


class CourseSubscriptionAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            email="test@example.com",
            password="password",
            phone="1234567890",  # если нужно
        )
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name="Test Course", description="Test Description"
        )

    def test_course_subscription_toggle(self):
        url = reverse("subscripe:course-subscribe")
        data = {"course_id": self.course.id}

        # Подписка на курс
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            CourseSubscription.objects.filter(
                user=self.user, course=self.course
            ).exists()
        )

        # Отписка от курса
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            CourseSubscription.objects.filter(
                user=self.user, course=self.course
            ).exists()
        )
