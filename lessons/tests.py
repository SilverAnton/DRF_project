from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from users.models import User
from courses.models import Course
from lessons.models import Lesson


class LessonAPITestCase(APITestCase):

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

        self.lesson = Lesson.objects.create(
            name="Test Lesson",
            description="Test Description",
            course=self.course,
            owner=self.user,
            video_link="https://youtube.com/test",
        )

    def test_lesson_creation(self):
        url = reverse("lessons:lesson_create")
        data = {
            "name": "New Lesson",
            "description": "New Description",
            "course": self.course.id,
            "video_link": "https://youtube.com/test2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_list(self):
        url = reverse("lessons:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_lesson_retrieve(self):
        url = reverse("lessons:lesson_retrieve", kwargs={"pk": self.lesson.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.lesson.name)

    def test_lesson_update(self):
        url = reverse("lessons:lesson_update", kwargs={"pk": self.lesson.id})
        data = {
            "name": "Updated Lesson",
            "description": "Updated Description",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.name, "Updated Lesson")

    def test_lesson_destroy(self):
        url = reverse("lessons:lesson_destroy", kwargs={"pk": self.lesson.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())
