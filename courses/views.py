from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from courses.paginations import CustomCoursePagination
from courses.serializer import CourseSerializer
from users.permissions import IsModeratorPermission, IsOwnerPermission
from subscriptions.tasks import send_course_update_emails


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomCoursePagination

    def perform_update(self, serializer):
        course = serializer.save()
        # Запуск асинхронной задачи после успешного обновления курса
        send_course_update_emails.delay(course.id)

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModeratorPermission,)
        elif self.action == "update" or self.action == "retrieve":
            self.permission_classes = (IsModeratorPermission | IsModeratorPermission,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModeratorPermission | IsOwnerPermission,)
        return super().get_permissions()
