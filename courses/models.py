from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course")
    image = models.ImageField(
        upload_to="images/course", verbose_name="Image", null=True, blank=True
    )
    description = models.TextField(verbose_name="Description")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Owner",
        related_name="courses",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
