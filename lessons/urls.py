from django.urls import path
from lessons.apps import LessonsConfig
from lessons.views import (
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    LessonDestroyApiView,
)

app_name = LessonsConfig.name

urlpatterns = [
    path("create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("", LessonListApiView.as_view(), name="lesson_list"),
    path("retrieve/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("update/<int:pk>/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("destroy/<int:pk>/", LessonDestroyApiView.as_view(), name="lesson_destroy"),
]
