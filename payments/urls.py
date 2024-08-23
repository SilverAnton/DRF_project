from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny

from rest_framework.routers import DefaultRouter

from payments.apps import PaymentsConfig
from payments.views import PaymentViewSet

router = DefaultRouter()
router.register("", PaymentViewSet)

app_name = PaymentsConfig.name
urlpatterns = []
urlpatterns += router.urls
