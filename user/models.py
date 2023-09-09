from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=50, verbose_name='Phone', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Country', **NULLABLE)

    email = models.EmailField(verbose_name='Email', unique=True)
    check_email = models.BooleanField(default=False, verbose_name='Check')
    verify_number = models.CharField(max_length=150, verbose_name='verify_number', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'view_users',
                'Can view users'
            ),
        ]



