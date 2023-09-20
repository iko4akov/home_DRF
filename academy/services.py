import os

import requests

from config import settings

class Payment:

    url = settings.URL_PAYMENT
    auth = (os.getenv('SECRET_KEY_PAYMENT'), '')

    def __init__(self, product_name, price_product):
        self.product_name = product_name
        self.price_product = price_product
        self.payment_url = self.__get_url_payment()
    def __get_url_payment(self):
        data = {
            "line_items[0][price]": self.__get_price(),
            "mode": 'payment',
            "success_url": 'https://stripe.com/docs/',
            "line_items[0][quantity]": 2
        }
        respounse = requests.post(url=self.url+'/checkout/sessions', auth=self.auth, data=data)

        return respounse.json()['url']

    def __get_product(self):
        data = {
            'name': self.product_name
        }
        respounse = requests.post(url=self.url+'/products', auth=self.auth, data=data)
        return respounse.json()['id']

    def __get_price(self):
        data = {
            'unit_amount': self.price_product,
            'currency': 'rub',
            'product': self.__get_product()
        }
        respounse = requests.post(url=self.url + '/prices', auth=self.auth, data=data)
        return respounse.json()['id']

