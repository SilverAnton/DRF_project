from django.db import models
from courses.models import Course
from users.models import User


class CourseSubscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="subscriptions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} -> {self.course.name}"

    class Meta:

        verbose_name = "Course Subscription"
        verbose_name_plural = "Course Subscriptions"
