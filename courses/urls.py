from django.urls import path
from django.views.decorators.cache import cache_page
from courses.apps import CoursesConfig
from rest_framework.routers import SimpleRouter

from courses.views import CourseViewSet

router = SimpleRouter()
router.register("", CourseViewSet)

app_name = CoursesConfig.name
urlpatterns = []
urlpatterns += router.urls
