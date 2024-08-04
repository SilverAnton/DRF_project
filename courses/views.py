from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from courses.models import Course
from courses.serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


