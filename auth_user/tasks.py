from celery import shared_task
from auth_user.models import User
from django.utils import timezone

@shared_task
def check_users():
    ten_days_ago = timezone.now() - timezone.timedelta(days=30)

    for user in User.objects.all().exclude(is_superuser=True, is_staff=True):
        if (not user.is_active and 
            not user.email_verification and 
            user.last_login is not None and 
            user.last_login < ten_days_ago):
            user.delete()