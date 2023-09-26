from datetime import datetime

from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail

from academy.models import Subscription
from config.settings import EMAIL_HOST_USER
from user.models import User


@shared_task
def mailer():
    subscribe = Subscription.objects.all()
    if len(subscribe) > 0:
        mailer_list = []
        for subscribe_items in subscribe:
            mailer_list.append(subscribe_items.user.email)

        send_mail(
            'Refresh',
            f'Refresh',
            from_email=EMAIL_HOST_USER,
            recipient_list=mailer_list
        )

def check_is_active():
    
    users = User.objects.filter(is_active=True)
    now = timezone.now().strftime("%Y-%m-%d")
    
    for user in users:
         different = datetime.fromisoformat(now) - datetime.fromisoformat(user.last_login)
         if different > 30:
             user.is_active = False
             user.save()
