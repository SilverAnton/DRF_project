from rest_framework import serializers
from lessons.models import Lesson
from lessons.validators import validate_video_link


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(
        validators=[validate_video_link], required=False, allow_blank=True
    )

    class Meta:
        model = Lesson
        fields = "__all__"
