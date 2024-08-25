from django.urls import path, include
from django.views.decorators.cache import cache_page


from django.urls import path

from payments.apps import PaymentsConfig
from payments.views import (
    CreateProductAPIView,
    CreatePriceAPIView,
    CreateCheckoutSessionAPIView,
)


app_name = PaymentsConfig.name
urlpatterns = [
    path("create-product/", CreateProductAPIView.as_view(), name="create-product"),
    path("create-price/", CreatePriceAPIView.as_view(), name="create-price"),
    path(
        "create-checkout-session/",
        CreateCheckoutSessionAPIView.as_view(),
        name="create-checkout-session",
    ),
]
