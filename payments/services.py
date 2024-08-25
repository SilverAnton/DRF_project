import requests
from django.conf import settings

STRIPE_API_BASE_URL = "https://api.stripe.com/v1/"


def get_headers():
    return {
        "Authorization": f"Bearer {settings.STRIPE_SECRET_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }


def create_product(name, description):
    url = f"{STRIPE_API_BASE_URL}products"
    data = {
        "name": name,
        "description": description,
    }
    response = requests.post(url, headers=get_headers(), data=data)
    response.raise_for_status()
    return response.json()


def create_price(product_id, amount):
    url = f"{STRIPE_API_BASE_URL}prices"
    data = {
        "unit_amount": amount * 100,
        "currency": "usd",
        "product": product_id,
    }
    response = requests.post(url, headers=get_headers(), data=data)
    response.raise_for_status()
    return response.json()


def create_checkout_session(price_id, success_url, cancel_url):
    url = f"{STRIPE_API_BASE_URL}checkout/sessions"
    data = {
        "payment_method_types[]": "card",
        "line_items[0][price]": price_id,
        "line_items[0][quantity]": 1,
        "mode": "payment",
        "success_url": success_url,
        "cancel_url": cancel_url,
    }
    response = requests.post(url, headers=get_headers(), data=data)
    response.raise_for_status()
    return response.json()
