from django.core.mail import send_mail
from django.conf import settings
from django.core import signing

def send_verification_email(user):
    token = signing.dumps(int(user.id))
    verify_url = f"http://127.0.0.1:8000/api/auth/verifications/?token={token}"
    subject = 'Подтверждение вашей электронной почты'
    message = f'Перейдите по ссылке для подтверждения вашей электронной почты: {verify_url}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)


def send_password_email(user):
    token = signing.dumps(int(user.id))
    verify_url = f"http://127.0.0.1:8000/api/auth/newpassword/?token={token}"
    subject = 'Подтверждение вашей электронной почты'
    message = f'Перейдите по ссылке для подтверждения вашей электронной почты: {verify_url}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

