from celery import shared_task
from django.core.mail import send_mail
import redis
from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None




@shared_task
def send_email_task():
    send_mail(
    '10 deqiqe qaldi ',
    'vaxt bitir',
    'anvarliorxan@gmail.com',
    ['anvarliorxan1@gmail.com'],
    fail_silently=False,
    )
    return None
    

    