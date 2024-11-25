import requests
import stripe
from rest_framework import status

from config.settings import CURRENCY_API_KEY, STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY
CURRENCY_API_KEY = CURRENCY_API_KEY


def convert_rub_to_usd(amount):
    usd_price = 90
    response = requests.get(
        f"https://api.currencyapi.com/v3/latest?apikey={CURRENCY_API_KEY}&currencies=RUB"
    )
    if response.status_code == status.HTTP_200_OK:
        usd_price = amount / response.json()["data"]["RUB"]["value"]
    return int(usd_price)


def create_stripe_price(amount, name):
    product = stripe.Product.create(name=name)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=product.id,
    )
    return price


def create_stripe_session(price):
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")