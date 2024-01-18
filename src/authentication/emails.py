from django.core.mail import send_mail
import random
from django.conf import settings
from .models import OurUser
from django.contrib.auth import authenticate


def send_otp_mail(email):
    otp = random.randint(1000, 9999)
    subject = 'OTP for email verification'
    message = f'Your OTP for email verification is {otp}'
    email_from = settings.EMAIL_HOST_USER

    recipient_list = [email]
    print(f"sending {email_from} to {recipient_list}")
    send_mail(subject, message, email_from, recipient_list)
    user_obj = OurUser.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
