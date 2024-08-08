from django.urls import path, include
from django.views.decorators.cache import cache_page
from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from users.views import UsersViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r"users", UsersViewSet)
router.register(r"payments", PaymentViewSet)


app_name = CoursesConfig.name
urlpatterns = [
    path("", include(router.urls))

]

