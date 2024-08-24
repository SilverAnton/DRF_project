from rest_framework.serializers import ModelSerializer, SerializerMethodField
from courses.models import Course
from lessons.models import Lesson
from lessons.serializers import LessonSerializer
from subscriptions.models import CourseSubscription


class CourseSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_is_subscribed(self, course):
        request = self.context.get("request", None)
        if request and request.user.is_authenticated:
            return CourseSubscription.objects.filter(
                user=request.user, course=course
            ).exists()
        return False
