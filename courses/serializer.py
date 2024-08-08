from rest_framework.serializers import ModelSerializer, SerializerMethodField
from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()





