import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from user.models import User


load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **options):
        list_user = [
            {'pk': 2, 'email': '2@2.com'},
            {'pk': 3, 'email': '3@3.com'},
            {'pk': 4, 'email': '4@4.com'},
        ]


        for item_user in list_user:

            new_user = User.objects.create(**item_user)

            new_user.set_password(item_user.get('email'))
            new_user.save()
