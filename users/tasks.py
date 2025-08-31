from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .utils import generate_confirmation_token

@shared_task
def send_register_email(user_id, email):
    token = generate_confirmation_token(user_id)

    send_mail(
        subject="Confirm your SignUp to VegeFoods",
        recipient_list=[email],
        message=f"""
Hi, please click this link to confirm your account registration:
http://127.0.0.1:8000/users/confirm/{token}
        """,
        from_email=settings.EMAIL_HOST_USER,
    )