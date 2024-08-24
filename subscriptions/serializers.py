from rest_framework import serializers
from subscriptions.models import CourseSubscription


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = "__all__"
