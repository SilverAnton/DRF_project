from django.db import models

from courses.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Lesson')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='image/lesson', verbose_name='Image', blank=True, null=True)
    video_link = models.URLField(verbose_name='Video Link',  blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course', related_name='lessons')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


