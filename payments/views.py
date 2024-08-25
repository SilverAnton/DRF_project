from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from payments.services import create_product, create_price, create_checkout_session


class CreateProductAPIView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        description = request.data.get("description")
        product = create_product(name, description)
        return Response(product, status=status.HTTP_201_CREATED)


class CreatePriceAPIView(APIView):
    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        amount = request.data.get("amount")
        price = create_price(product_id, amount)
        return Response(price, status=status.HTTP_201_CREATED)


class CreateCheckoutSessionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        price_id = request.data.get("price_id")
        success_url = request.data.get("success_url")
        cancel_url = request.data.get("cancel_url")
        session = create_checkout_session(price_id, success_url, cancel_url)
        return Response({"id": session["id"]}, status=status.HTTP_201_CREATED)
