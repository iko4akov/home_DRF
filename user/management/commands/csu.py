import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from user.models import User


load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **options):

        super_user = User.objects.create(
            email='admin@admin.com',
            country='United',
            phone='12345678910',
            is_staff=True,
            is_superuser=True,
        )

        super_user.set_password(os.getenv('PASSWORD_SU'))
        super_user.save()
